# 08-magicsquare-tdd-readme-todo-draft Report

## 작업 배경/목표

- Magic Square 4x4 TDD Practice 프로젝트의 **구현 착수 전** 산출물을 문서화한다.
- PRD(`docs/PRD_MagicSquare.md`)를 기반으로 **개발 To-Do List(추적 보드)** 와 **README.md 초안**을 작성한다.
- Dual-Track UI + Logic TDD, ECB, Scenario → AC → RED → GREEN → REFACTOR 추적 구조를 고정한다.
- 구현 코드·테스트 코드·기타 파일 생성은 수행하지 않는다.

## 수행 내용

### Turn 1 — 개발 To-Do List 작성 (파일 미저장)

- 역할: Senior Software Architect + Dual-Track UI + Logic TDD 코치
- 참고 문서 확인:
  - `docs/PRD_MagicSquare.md`
  - `Report/06-magicsquare-user-journey-level1-5_Report.md`
  - `Report/02-tdd-design-report.md`
  - `Report/03-cursorrules-work-report.md`
  - `.cursorrules`, `.cursor/rules/*.mdc`
- 사용자 지정 출력 구조에 맞춰 Markdown 본문만 출력:
  1. Epic (Epic-001)
  2. User Stories (US-001 ~ US-007)
  3. Scenario → AC → RED → GREEN Tracking Board (TASK-001 ~ TASK-023, 23행)
  4. RED Start Checklist (11항)
  5. Traceability Summary (필수 Concept/Invariant 16항)
- 반드시 포함 Scenario 15건 모두 매핑:
  - None 입력, 비 4×4, 빈칸 개수, 값 범위, 중복, row-major 빈칸, 누락 숫자 오름차순
  - 행/열/대각선 합 34, small-first, reverse, 두 조합 실패, int[6], 1-index
- RED는 「실패 상태 확인」, GREEN/REFACTOR는 후보로만 기술
- Dual-Track 분리: Boundary RED / Logic RED / Integration RED
- 권장 RED 착수 순서 및 미확정 사항(DN-04, DN-05) 명시

### Turn 2 — README.md 초안 작성 (파일 미저장)

- 역할: Technical Writer + Dual-Track UI + Logic TDD 코치
- 사용자 지정 10개 섹션 구조에 맞춰 README Markdown 본문만 출력:
  1. Project Start Declaration
  2. PRD Summary
  3. TDD Development Flow (8단계)
  4. Development Methodology
  5. ECB Role Separation (표)
  6. Scenario → AC → RED → GREEN Tracking Board (15 Scenario, 15행)
  7. RED Start Checklist
  8. Quality Gates
  9. Reference Documents (실제 경로 병기)
  10. Current Project Status
- `pyproject.toml` 미존재 확인 — Quality Gates에 「예정 도구 설정」으로 기록
- 문서 간 관계 다이어그램 포함 (01 → 02 → 06 → PRD → 03/05 → README)

### Turn 3 — 보고서/백업 (본 Turn)

- `report-backup-agent` 지침에 따라 Report/Prompting **08**번 문서 쌍 생성

## 생성/수정 파일 목록

| 구분 | 경로 |
|------|------|
| 생성 | `Report/08-magicsquare-tdd-readme-todo-draft_Report.md` (본 문서) |
| 생성 | `Prompting/08-magicsquare-tdd-readme-todo-draft_Prompt.md` |
| **미생성** | `README.md` (초안은 채팅 출력만, 파일 저장 안 함) |
| **미생성** | To-Do List 파일 (채팅 출력만) |
| **미생성** | 구현 코드, 테스트 코드, `pyproject.toml` |

## 검증 결과

- To-Do List: 사용자 필수 Scenario 15건 + 추가 Integration/품질 Task 포함 확인
- README: 사용자 필수 10섹션·15 Scenario Tracking Board 포함 확인
- TDD 게이트 표현: RED = 테스트 실패 상태 확인, GREEN/REFACTOR = 후보만 — 일관 적용
- ECB Layer·Code Target·RED Test ID 형식(RED-BND-*, RED-DOM-*) PRD §15·§23.4와 정합
- 파일 생성 제약: Turn 1·2에서 코드/테스트/파일 생성 없음 — 준수

## 남은 이슈 및 다음 액션

1. **README.md 파일 저장** — Turn 2 출력 본문을 루트 `README.md`에 반영 (사용자 지시 시)
2. **To-Do List 영구 저장** — 필요 시 `docs/` 또는 `Report/`에 별도 문서로 저장
3. **TD-SUCCESS-REV-001** 수치 확정 (PRD DN-04) — reverse 성공 RED 착수 전
4. **ResultFormatter Layer** 결론 (PRD DN-05) — Boundary vs Control
5. **`pyproject.toml` 생성** — pytest, pytest-cov, ruff/black 설정
6. **다음 단계**: Test Skeleton 작성 → `pytest` 실행 → RED 실패 확인 → Dual-Track 교차 GREEN

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | To-Do List·README 초안 세션 백업 |
