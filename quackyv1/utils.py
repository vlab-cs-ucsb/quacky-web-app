import re
import sys
import time

from .utilities.Shell import Shell # courtesy of VLab

shell = Shell()

# Quacky source directory
QUACKY_DIR = "/home/ganesh/Desktop/quacky/src"

FAILURE = {
    'is_single': True,
    'status': 'Failure'
}

SINGLE_STUB = {
    'is_single': True,
    'status': 'Success',
    'solve_time': '420.0',
    'is_sat': 'SAT',
    'count_time': '69.0',
    'count': '12345',
    'var': {
        'x': {
            'count': '1',
            'count_time': '1.0'
        },
        'y': {
            'count': '2',
            'count_time': '2.0'
        }
    }
}

MULTI_STUB = ({
    'status': 'Success',
    'solve_time': '420.0',
    'is_sat': 'SAT',
    'count_time': '69.0',
    'count': '12345',
    'var': {
        'x': {
            'count': '1',
            'count_time': '1.0'
        },
        'y': {
            'count': '2',
            'count_time': '2.0'
        }
    }
}, {
    'status': 'Success',
    'solve_time': '420.0',
    'is_sat': 'SAT',
    'count_time': '69.0',
    'count': '12345',
    'var': {
        'x': {
            'count': '1',
            'count_time': '1.0'
        },
        'y': {
            'count': '2',
            'count_time': '2.0'
        }
    }
})

def ta_aws_single(d):
    # Create policy
    fname = str(int(round(time.time() * 1000)))

    f = open(fname + '.json', 'w')
    f.write(d['policy1'])
    f.close()

    global shell
    out, err = shell.mv(fname + '.json', QUACKY_DIR)

    # Translate policy
    cmd = 'python3 translate_policy.py -p1 {0}.json -o {0}'.format(fname)

    if d['constraints']:
        cmd += ' -c'
    if d['encoding']:
        cmd += ' -e'

    out, err = shell.runcmd(cmd, cwd=QUACKY_DIR)

    # Solve SMT formula
    results = get_results(fname + '_1.smt2', d['bound'], 30)
    results['is_single'] = True

    # Clean up
    out, err = shell.rm('{}/{}.json'.format(QUACKY_DIR, fname))
    out, err = shell.rm('{}/{}_0.smt2'.format(QUACKY_DIR, fname))
    out, err = shell.rm('{}/{}_1.smt2'.format(QUACKY_DIR, fname))

    return results

def ta_aws_multi(d):
    # Create policies
    fname = str(int(round(time.time() * 1000)))

    f = open(fname + '1.json', 'w')
    f.write(d['policy1'])
    f.close()

    f = open(fname + '2.json', 'w')
    f.write(d['policy2'])
    f.close()

    global shell
    out, err = shell.mv(fname + '1.json', QUACKY_DIR)
    out, err = shell.mv(fname + '2.json', QUACKY_DIR)

    # Translate policies
    cmd = 'python3 translate_policy.py -p1 {0}1.json -p2 {0}2.json -o {0}'.format(fname)

    if d['constraints']:
        cmd += ' -c'
    if d['encoding']:
        cmd += ' -e'

    out, err = shell.runcmd(cmd, cwd=QUACKY_DIR)

    # Solve SMT formulas
    results1 = get_results(fname + '_1.smt2', d['bound'], 30)
    results2 = get_results(fname + '_2.smt2', d['bound'], 30)

    # Clean up
    out, err = shell.rm('{}/{}1.json'.format(QUACKY_DIR, fname))
    out, err = shell.rm('{}/{}2.json'.format(QUACKY_DIR, fname))
    out, err = shell.rm('{}/{}_0.smt2'.format(QUACKY_DIR, fname))
    out, err = shell.rm('{}/{}_1.smt2'.format(QUACKY_DIR, fname))
    out, err = shell.rm('{}/{}_2.smt2'.format(QUACKY_DIR, fname))

    return (results1, results2)

def ta_azure(d):
    return SINGLE_STUB

def ta_gcp(d):
    return SINGLE_STUB

def get_results(fname, bound, timeout):
    cmd = 'timeout -k {0}s {0}s'.format(timeout)
    cmd += ' abc -i {}'.format(fname)
    cmd += ' -bs {0} -bi {0}'.format(bound)
    cmd += ' --count-tuple --count-variable principal,action,resource -v 0'
    
    out, err = shell.runcmd(cmd, cwd=QUACKY_DIR)

    # Parse ABC output
    results = get_abc_result_line(out, err)
    results['out'] = out
    results['err'] = err

    if 'is_sat' in results.keys() and 'solve_time' in results.keys():
        results['status'] = 'Success'
    elif 'SIGTERM' in results['err']:
        results['status'] = 'Timeout'
    else:
        results['status'] = 'Failure'
    
    if 'count' in results.keys() and int(results['count']) > sys.maxsize:
        try:
            results['count'] = format(int(results['count']), '9.6e')
        except:
            pass
    
    if 'var' in results.keys():
        for var in results['var'].keys():
            if int(results['var'][var]['count']) > sys.maxsize:
                try:
                    results['var'][var]['count'] = format(int(results['var'][var]['count']), '9.6e')
                except:
                    pass

    return results


# Parse ABC output (courtesy of VLab)
def get_abc_result_line(out, err):
    lines = err.strip(' \t\n\r,').split('\n')
    var_results = {}
    results = {}
    for line in lines:
        match = re.match(
            r".*report is_sat:\s*(?P<is_sat>\w+)\s*time:\s*(?P<time>\d+(\.\d+)*)\s*ms\s*", line, re.IGNORECASE)
        if match:
            results["is_sat"] = match.group('is_sat')
            results["solve_time"] = match.group('time')
            continue

        match = re.match(
            r".*report \(TUPLE\) bound:\s*(?P<bound>\d+)\s*count:\s*(?P<count>\d+)\s*time:\s*(?P<time>\d+(\.\d+)*)\s*ms\s*", line, re.IGNORECASE) 
        if match:
            results["bound"] = match.group('bound')
            results["count"] = match.group('count')
            results["count_time"] = match.group('time')

        match = re.match(
            r".*report bound:\s*(?P<bound>\d+)\s*count:\s*(?P<count>\d+)\s*time:\s*(?P<time>\d+(\.\d+)*)\s*ms\s*", line, re.IGNORECASE)
        if match:
            if "var" in results:
                var_results[results["var"]] = {"bound": match.group('bound'), "count": match.group('count'), "count_time": match.group('time')}
            continue

        match = re.match(r".*report var:\s*(?P<var>.+)\s*", line, re.IGNORECASE)
        if match:
            results["var"] = match.group('var')
            continue

    results["var"] = var_results
    return results