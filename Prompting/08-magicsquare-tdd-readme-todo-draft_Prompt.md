# 08-magicsquare-tdd-readme-todo-draft Prompt

## 세션 개요

- **주제**: Magic Square 4x4 TDD Practice — 개발 To-Do List 및 README.md 초안 작성
- **목적**: PRD 기반 TDD 시작 준비; Scenario → AC → RED → GREEN → REFACTOR 추적 보드·개발 가이드 고정
- **제약**: 구현 코드·테스트 코드·파일 생성 금지; Markdown 본문 출력만

## Turn Transcript

### Turn 1

**User**

- Senior Software Architect + Dual-Track UI + Logic TDD 코치 역할
- PRD 기반 **개발 To-Do List** 작성 (단순 작업 목록이 아닌 TDD 추적 보드)
- 흐름: Scenario → AC → RED Test ID → Test Skeleton → Run Test → Confirm Failure(RED) → GREEN Task → REFACTOR
- 필수 Scenario 15건, Epic/User Story/Tracking Board/RED Checklist/Traceability Summary 포함
- 참고: `docs/5.PRD_MagicSquare_4x4_TDD.md`, Report/2,3,4, `.cursorrules`, `.cursor/rules/*.mdc`
- **구현·테스트·파일 생성 금지** — To-Do List Markdown 본문만 출력

**Assistant**

- `docs/PRD_MagicSquare.md`, Report/02, 03, 06, `.cursorrules`, ECB 규칙 읽기
- `# MagicSquare 4x4 개발 To-Do List` 전체 Markdown 출력:
  - Epic-001, US-001~007
  - Tracking Board TASK-001~023 (Boundary/Logic/Integration RED)
  - RED Start Checklist 11항
  - Traceability Summary 16 Concept/Invariant
- 권장 RED 착수 순서, DN-04/DN-05 미확정 사항 명시

---

### Turn 2

**User**

- Technical Writer + Dual-Track TDD 코치 역할
- PRD 기반 **README.md 초안** 작성 (프로젝트 시작 선언 + 개발 가이드)
- 10개 섹션: Project Start, PRD Summary, TDD Flow, Methodology, ECB, Tracking Board(15 Scenario), Checklist, Quality Gates, References, Status
- 참고: PRD, Report/1~4, `pyproject.toml`, `.cursorrules`, Report/5
- **구현·테스트·파일 생성 금지** — README Markdown 본문만 출력

**Assistant**

- `pyproject.toml` 미존재 확인 (Glob 0건)
- Report/05-cursor-agents-expansion 존재 확인
- `# MagicSquare 4x4 TDD Practice` README 전체 Markdown 출력:
  - 8단계 TDD Flow 표
  - ECB Role Separation 표
  - Tracking Board 15행 (필수 Scenario 전부)
  - Quality Gates (Domain 95%+, Boundary 85%+, pytest AAA 등)
  - Reference Documents 실제 경로 병기 + 문서 간 관계 다이어그램
  - Current Status: 구현·테스트 전, 다음 단계 Test Skeleton + RED

---

### Turn 3

**User**

- `@.cursor/agents/report-backup-agent.md` 보고서/백업 요청

**Assistant**

- report-backup-agent 지침 확인
- Report/Prompting 최대 번호 07 → **08** 발급
- `Report/08-magicsquare-tdd-readme-todo-draft_Report.md` 생성
- `Prompting/08-magicsquare-tdd-readme-todo-draft_Prompt.md` 생성 (본 파일)

---

## 최종 결과 요약

- PRD 기반 **TDD 추적 To-Do List**(23 Task)와 **README 초안**(10섹션, 15 Scenario 보드)을 채팅으로 산출했다.
- README·To-Do List는 **파일로 저장되지 않았다** — 사용자가 복사·저장 지시 시 반영 가능.
- 프로젝트 상태: PRD 기반 TDD 시작 준비, 구현·테스트·RED 확인 전.
- 다음 단계: Test Skeleton 작성 및 `pytest`로 RED 실패 확인.
