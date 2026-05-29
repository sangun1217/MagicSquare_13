# MagicSquare Cursor Rule 작업 보고서

## 1) 작업 개요
- 목적: MagicSquare Python 프로젝트용 `.cursorrules` 규칙 체계를 설계/작성하고, TDD/ECB/테스트 금지사항을 구조화
- 범위: 규칙 구조 설계 설명, YAML 뼈대 작성, 상세 섹션 확장, 점검 및 보완
- 기준: Python 3.10+, PEP8, type hints 필수, pytest AAA, ECB, Dual-Track TDD

## 2) 수행 내용
- `.cursorrules` 초기 뼈대 생성 (`project`, `code_style`, `architecture`, `tdd_rules`, `testing`, `forbidden`, `file_structure`, `ai_behavior`)
- `tdd_rules`를 RED/GREEN/REFACTOR 하위 구조로 세분화
- 전체 섹션을 MagicSquare 기준 정책으로 확장
  - `code_style`: Python 3.10+, PEP8, type hints, Google docstring, line length 88
  - `architecture`: ECB 3계층 역할과 의존성 방향 명시
  - `testing`: pytest, AAA, coverage 80%, fixture scope 규칙, naming 규칙
  - `forbidden`: 금지 패턴/사유/대안 구조로 정리
  - `file_structure`: ECB 중심 트리 주석 및 디렉터리 매핑
  - `ai_behavior`: 코드 작성 전/중/후/위반 시 행동 규칙화

## 3) 점검 결과
- YAML 문법: 확인된 오류 없음
- 필수 섹션: 누락 없음
- `tdd_rules` ↔ `forbidden` 충돌: 확인된 충돌 없음
- 실행 불가 규칙 1건 보완:
  - 기존: `RED 증거가 있는가?`
  - 변경: `RED 단계 수행 시 실패 테스트 실행 결과(명령/요약)를 작업 로그에 남겼는가?`

## 4) 산출물
- 규칙 파일: `.cursorrules`
- 본 보고서: `Report/03-cursorrules-work-report.md`
- 대화 transcript: `Prompt/export-transcript-cursorrules-2026-05-28.md`

## 5) 후속 권장
- `.cursorrules`를 `.cursor/rules/*.mdc`로 분해해 유지보수성 향상
- `pytest`/`coverage`/`ruff`/`black` 설정을 실제 CI와 동기화
- ECB 의존성 위반을 정적 검사 또는 리뷰 체크리스트로 고정화
