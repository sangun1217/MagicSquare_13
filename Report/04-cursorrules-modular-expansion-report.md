# MagicSquare Cursor Rules 모듈 확장 보고서

## 1) 작업 목적
- 기존 단일 `.cursorrules` 기반 규칙을 유지하면서, `.cursor/rules/*.mdc` 구조로 확장해 규칙을 체계적으로 관리한다.
- 규칙 주제별 책임을 분리해 수정/검토/재사용 편의성을 높인다.

## 2) 수행 내역
- 다음 모듈형 규칙 파일을 신규 생성했다.
  - `.cursor/rules/magicsquare-project.mdc`
  - `.cursor/rules/magicsquare-python-code-style.mdc`
  - `.cursor/rules/magicsquare-ecb-architecture.mdc`
  - `.cursor/rules/magicsquare-tdd-testing.mdc`
  - `.cursor/rules/magicsquare-forbidden.mdc`

## 3) 파일별 역할
- `magicsquare-project.mdc`
  - 프로젝트 공통 목표/우선순위/비타협 원칙 정의
- `magicsquare-python-code-style.mdc`
  - Python 3.10+, PEP8, 타입힌트, docstring 등 코드스타일 규칙
- `magicsquare-ecb-architecture.mdc`
  - ECB 레이어 책임과 허용/금지 의존성 방향 명시
- `magicsquare-tdd-testing.mdc`
  - Dual-Track TDD(RED/GREEN/REFACTOR), pytest AAA, coverage/fixture 규칙
- `magicsquare-forbidden.mdc`
  - 금지 패턴과 이유/대안 정리

## 4) 운영 방식
- 하이브리드 전략 유지:
  - `.cursorrules`: 상위 프로젝트 정책/체크포인트
  - `.cursor/rules/*.mdc`: 주제별 상세 실행 규칙
- 변경 시 해당 주제 파일만 수정해 영향 범위를 제한한다.

## 5) 점검 결과
- `.cursor/rules` 내 `.mdc` 파일 5개 존재 확인
- 생성 직후 진단에서 별도 lint 오류 없음

## 6) 후속 권장
- `.cursorrules`와 `.mdc` 간 중복 문구를 단계적으로 줄여 단일 출처를 명확화
- 테스트/아키텍처 규칙은 CI 체크리스트와 연계해 실효성 강화
