import ast, json, re, sys
from pathlib import Path


def evaluate(path):
    source = Path(path).read_text(encoding='utf-8')
    rubric = json.loads(Path(__file__).with_name('rubric.json').read_text())
    score = 0
    checks = {}
    try:
        ast.parse(source); checks['syntax'] = True; score += 25
    except SyntaxError:
        checks['syntax'] = False
    checks['tests'] = bool(re.search(r'(pytest|unittest|def test_)', source)); score += 15 if checks['tests'] else 0
    checks['empty_input'] = bool(re.search(r'(strip\(\)|if not |not .*input|empty)', source)); score += rubric['Edge Cases'] if checks['empty_input'] else 0
    checks['error_handling'] = bool(re.search(r'(try:|except |raise |status_code|ValueError)', source)); score += (rubric['Code Quality'] if '```' in source else 12) if checks['error_handling'] else 0
    checks['security'] = not bool(re.search(r'(eval\(|exec\(|shell=True)', source)); score += rubric['Security'] if checks['security'] else 0
    return min(score, 100), checks

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python evaluator.py CODE_FILE')
    score, checks = evaluate(sys.argv[1])
    print(json.dumps({'score': score, 'checks': checks}, indent=2))
