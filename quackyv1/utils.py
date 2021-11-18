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

def ta_azure_single(d):
    # Create policy
    fname = str(int(round(time.time() * 1000)))

    policy = azure2policy(d)

    if not policy:
        return FAILURE

    f = open(fname + '.json', 'w')
    f.write(policy) # Convert Azure stuff to policy model
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

def ta_azure_multi(d):
    # Create policies
    fname = str(int(round(time.time() * 1000)))

    policies = azure2policy(d, multi=True)

    if not policies:
        return FAILURE

    f = open(fname + '1.json', 'w')
    f.write(policies[0])
    f.close()

    f = open(fname + '2.json', 'w')
    f.write(policies[1])
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


def ta_gcp(d):
    # Create policy
    fname = str(int(round(time.time() * 1000)))

    policy = gcp2policy(d)

    if not policy:
        return FAILURE

    f = open(fname + '.json', 'w')
    f.write(policy) # Convert GCP stuff to policy model
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

def azure2policy(d, multi=False):
    # Too lazy to check for ill-formed role definitions/assignments
    try:
        role_definitions = json.loads(d['role_definitions'])
        role_assignment1 = json.loads(d['role_assignment1'])

        if not multi:
            return azure2policy_helper(role_definitions, role_assignment1)
        else:
            role_assignment2 = json.loads(d['role_assignment2'])
            return (azure2policy_helper(role_definitions, role_assignment1),
                    azure2policy_helper(role_definitions, role_assignment2))
    
    except:
       return None


def azure2policy_helper(role_definitions, role_assignment):
    statements = []
        
    for ra in role_assignment:
        for rd in role_definitions:
            if ra['properties']['roleDefinitionId'] == rd['Id']:
                
                statement = {
                    'Id': rd['Id'],
                    'Effect': 'Allow',
                    'Principal': ra['properties']['principalId'],
                    'Action': [a.lower() for a in rd['Actions'] + rd['DataActions']],
                }

                if len(rd['NotActions'] + rd['NotDataActions']) > 0:
                    statement['NotAction']: [a.lower() for a in rd['NotActions'] + rd['NotDataActions']]

                if ra['scope'].count('/') <= 6:
                    statement['Resource'] = ra['scope'].lower() + '/*'
                else:
                    statement['Resource'] = ra['scope'].lower()
                
                if 'condition' in ra['properties']:
                    statement['Condition'] = ra['properties']['condition']

                statements.append(statement)
        
    return json.dumps({'Version': 'azure', 'Statement': statements}, indent=4)

def gcp2policy(d):
    # Too lazy to check for ill-formed role (bindings)
    try:
        role = json.loads(d['role'])
        role_bindings = json.loads(d['role_bindings'])

        statements = []

        for rb in role_bindings['bindings']:
            for rd in role:
                if rb['role'] == rd['name']:
                    
                    statement = {
                        'Id': rd['title'],
                        'Effect': 'Allow',
                        'Principal': rb['members'],
                        'Action': [a.lower() for a in rd['includedPermissions']],
                    }

                    if rb['level'].count('/') <= 2:
                        statement['Resource'] = rb['level'].lower() + '/*'
                    else:
                        statement['Resource'] = rb['level'].lower()

                    if 'condition' in rb:
                        statement['Condition'] = rb['condition']['expression'].lower()

                    statements.append(statement)

        return json.dumps({'Version': 'gcp', 'Statement': statements}, indent=4)
    
    except:
        return None

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