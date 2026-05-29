# 07-magicsquare-prd-and-review Prompt

## 세션 개요

- **주제**: Magic Square 4x4 TDD Practice — PRD 작성, 저장, 7기준 검토
- **목적**: Dual-Track TDD / ECB / Traceability를 반영한 구현 전 기준 문서(PRD) 확정 및 품질 점검
- **제약**: 구현 코드·테스트 코드 작성 금지; PRD 1차는 Markdown 본문만, 이후 파일 저장 지시

## Turn Transcript

### Turn 1

**User**

- Senior Product/Software Architect 역할로 Magic Square 4x4 PRD 작성 요청
- Dual-Track UI + Logic TDD, Clean Architecture, ECB, Concept-to-Code Traceability 반영
- 23개 섹션 구조, 고정 I/O 계약, FR-01~05, Traceability Matrix 필수
- 참고: Report/1,2,3,4 및 `.cursorrules`, `.cursor/rules/*.mdc`
- **파일 생성 금지** — `docs/PRD_MagicSquare.md` 저장 가능한 Markdown 본문만 출력

**Assistant**

- Report/01, 02, 03, 06 및 Cursor Rules 읽기
- 23섹션 PRD 전체 Markdown 출력
- ERR-VAL-001~004, ERR-SOL-001, Dual-Track Strategy, Traceability Matrix 포함
- DN-01~06 Decision Needed 표기
- TD-SUCCESS-SF-001 구체 예시 `[1,1,1,4,4,16]` 제공

---

### Turn 2

**User**

- PRD 본문을 `docs/PRD_MagicSquare.md`에 파일로 저장 요청

**Assistant**

- `docs/` 디렉터리 생성
- `docs/PRD_MagicSquare.md` 저장 (653 lines)
- 참고 문서 링크 `../Report/...` 상대 경로 적용

---

### Turn 3

**User**

- 작성한 PRD를 7개 기준으로 검토 요청
  1. FR별 테스트 가능 AC
  2. AC ↔ Traceability Matrix
  3. Boundary/Domain 책임 혼합
  4. 오류 정책 미정
  5. small-first / reverse 테스트 데이터 구분
  6. 1-index / row-major 누락
  7. 구현·테스트 코드 미포함
- **수정 금지**, 문제와 개선안만 보고

**Assistant**

- `docs/PRD_MagicSquare.md` 전문 읽기 후 검토 보고서 출력
- 7기준 판정표: 1项 충족, 5项 부분/미충족
- P1~P6 이슈 ID, 우선순위별 개선 권고 6항 제시
- 교차 이슈 mermaid 다이어그램 포함

---

### Turn 4

**User**

- `@.cursor/agents/report-backup-agent.md` 보고서/백업 요청

**Assistant**

- report-backup-agent 지침 확인
- Report/Prompting 최대 번호 06 → **07** 발급
- `Report/07-magicsquare-prd-and-review_Report.md` 생성
- `Prompting/07-magicsquare-prd-and-review_Prompt.md` 생성 (본 파일)

## 최종 결과 요약

- **산출물**: `docs/PRD_MagicSquare.md` (PRD v1.0 Draft)
- **검토**: RED 착수 전 보완 필요 — REV fixture 미확정, Layer 모순(1-index), Matrix AC 누락
- **다음 단계**: PRD v1.1 개정 → TD-SUCCESS-REV-001 확정 → Level 6 RED 설계
