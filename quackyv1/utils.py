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

def ta_aws_single(policy1):
    return SINGLE_STUB

def ta_aws_multi(policy1, policy2):
    return MULTI_STUB

def ta_azure(rd, ra):
    return SINGLE_STUB

def ta_gcp(role, rb):
    return SINGLE_STUB