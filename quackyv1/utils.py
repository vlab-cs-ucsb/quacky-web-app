import decimal
import json
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

def ta_aws_single(d):
    try:
        # Create policy
        fname = str(int(round(time.time() * 1000)))
        write_file(fname, d['policy1'])

        # Translate policy
        cmd = 'python3 translator.py -p1 {0}.json -o {0}'.format(fname)
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

    except Exception as e:
        print(e)
        return FAILURE

def ta_aws_multi(d):
    try:
        # Create policies
        fname = str(int(round(time.time() * 1000)))
        write_file(fname + '1', d['policy1'])
        write_file(fname + '2', d['policy2'])

        # Translate policies
        cmd = 'python3 translator.py -p1 {0}1.json -p2 {0}2.json -o {0}'.format(fname)
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

    except Exception as e:
        print(e)
        return FAILURE

def ta_azure_single(d):
    try:
        # Create policy
        fname = str(int(round(time.time() * 1000)))
        write_file(fname + 'rd', d['role_definitions'])
        write_file(fname + 'ra1', d['role_assignment1'])

        # Translate policy
        cmd = 'python3 translator.py -rd {0}rd.json -ra1 {0}ra1.json -o {0}'.format(fname)
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

    except Exception as e:
        print(e)
        return FAILURE

def ta_azure_multi(d):
    try:
        # Create policies
        fname = str(int(round(time.time() * 1000)))
        write_file(fname + 'rd', d['role_definitions'])
        write_file(fname + 'ra1', d['role_assignment1'])
        write_file(fname + 'ra2', d['role_assignment2'])

        # Translate policies
        cmd = 'python3 translator.py -rd {0}rd.json -ra1 {0}ra1.json -ra2 {0}ra2.json -o {0}'.format(fname)
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

    except Exception as e:
        print(e)
        return FAILURE

def ta_gcp_single(d):
    try:
        # Create policy
        fname = str(int(round(time.time() * 1000)))
        write_file(fname + 'r', d['role'])
        write_file(fname + 'rb1', d['role_bindings1'])

        # Translate policy
        cmd = 'python3 translator.py -r {0}r.json -rb1 {0}rb1.json -o {0}'.format(fname)
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
    
    except Exception as e:
        print(e)
        return FAILURE

def ta_gcp_multi(d):
    try:
        # Create policies
        fname = str(int(round(time.time() * 1000)))
        write_file(fname + 'r', d['role'])
        write_file(fname + 'rb1', d['role_bindings1'])
        write_file(fname + 'rb2', d['role_bindings2'])

        # Translate policies
        cmd = 'python3 translator.py -r {0}r.json -rb1 {0}rb1.json -rb2 {0}rb2.json -o {0}'.format(fname)
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

    except Exception as e:
        print(e)
        return FAILURE

def write_file(fname, body):
    f = open(fname + '.json', 'w')
    f.write(body)
    f.close()

    global shell
    out, err = shell.mv(fname + '.json', QUACKY_DIR)

    return out, err

def get_variables(fname):
    formula = open(QUACKY_DIR + '/' + fname, 'r').read()
    variables = []

    for dtype in ['String', 'Int']:
        pattern = 'declare-const ([A-Za-z0-9\.]+) {}'.format(dtype)
        variables += re.findall(pattern, formula)

    return variables

def get_results(fname, bound, timeout):
    variables = get_variables(fname)

    cmd = 'timeout -k {0}s {0}s'.format(timeout)
    cmd += ' abc -i {}'.format(fname)
    cmd += ' -bs {0} -bi {0}'.format(bound)
    cmd += ' --count-tuple --count-variable {} -v 0'.format(','.join(variables))
    
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
        results['count'] = format(decimal.Decimal(results['count']), '.3e')
    
    if 'var' in results.keys():
        for var in results['var'].keys():
            if int(results['var'][var]['count']) > sys.maxsize:
                try:
                    results['var'][var]['count'] = format(decimal.Decimal(results['var'][var]['count']), '.3e')
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