# 17-ecb-refactor-plan-analysis Prompt Transcript

## 세션 개요

- **주제:** ECB 매핑 파일 코드 스멜 · 역할 적합성 · SRP · REFACTOR 계획
- **모드:** Ask (코드 수정 없음)
- **대상 파일:** `solve_partial_magic_square.py`, `ui_boundary.py`, `main_window.py`(미존재)
- **참고:** `input_validator.py`, `entity/solver.py`, `.cursorrules`

---

## Turn 1

**User**  
`solve_partial_magic_square.py`, `ui_boundary.py`, `main_window.py` 점검 — 이름, 중복, 긴 함수, 매직넘버, 파라미터 4+, 불필요 주석, 미사용 코드, 예외 오류, 무시 반환값, ECB 책임 혼재. 표 형식 High→Medium→Low.

**Assistant**  
실제 경로 `src/magicsquare/` 확인. `main_window.py` 미존재. High: `UnsolvableDomainError` Boundary 누출, Screen 부재. Medium: Control pass-through, type alias 중복, ResultFormatter 미사용 등. Low: 타입·이름 이슈.

---

## Turn 2

**User**  
ECB 매핑(domain/boundary/gui → 실제 파일). Control vs Entity, Boundary must_not, main_window UI 외 책임. 잘못된 위치 코드 이동표, Control/Entity 혼재, REFACTOR 1순위, P0/P1 순서.

**Assistant**  
- Control: 부분 적합(pass-through). Entity `solver.py`에 오케스트레이션·int[6] 조립 혼재.  
- Boundary: E001~E005 OK, E006/E007·schema 미완.  
- P0: Control 이동, Boundary envelope, U-FLOW/U-OUT 테스트 갭.  
- P1: ResultFormatter, two_cell_solver, main_window, solve_entry 제거.

---

## Turn 3

**User**  
SRP 위반만 표로: ① 함수 다중 역할 ② 클래스 데이터+검증 ③ UI 비즈니스 판단.

**Assistant**  
- ① `ui_boundary.py:26-41` 검증 게이트 + Control 위임.  
- ② 데이터+검증 혼재 해당 없음; `UIBoundary` 클래스 복수 책임.  
- ③ main_window 해당 없음(미존재).

---

## Turn 4

**User**  
리팩토링 계획서 — 대상 목록(우선순위), 테스트 선행, 회귀 검증 방법.

**Assistant**  
순번 1~10 REFACTOR 대상(P0~P3), 테스트 선행 함수 목록(Characterization·U-FLOW·U-OUT·GM), `pytest -ra` / `-m golden_master` / coverage 게이트 정리.

---

## Turn 5

**User**  
report-backup-agent 리포트/백업, GitHub 업로드.

**Assistant**  
Ask mode로 파일·push 불가 → Agent mode 전환 요청.

---

## Turn 6

**User**  
리포트/백업하고 GitHub에 올려줘.

**Assistant**  
Report/17·Prompting/17 생성, Report/16·Prompting/16 포함 커밋, `origin/develop` push.

---

## 최종 결과 요약

- ECB REFACTOR 전 분석·계획 문서화 완료.
- 코드 변경 없음; 다음 단계는 P0 테스트 선행 → Control/Boundary 구조 분리.
- 산출물: `Report/17-ecb-refactor-plan-analysis_Report.md`, `Prompting/17-ecb-refactor-plan-analysis_Prompt.md`
