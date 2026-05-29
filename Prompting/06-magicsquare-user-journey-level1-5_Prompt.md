# 06-magicsquare-user-journey-level1-5 Prompt

## 세션 개요
- 주제: Magic Square 4x4 TDD Practice의 Level 1~5 문서화
- 목적: Epic -> Journey -> Story -> Technical Scenario -> Verification 체계를 단계별로 정리
- 제약: 구현 코드/테스트 코드/파일 생성 지시가 없는 단계에서는 문서 산출만 수행

## Turn Transcript

### Turn 1
**User**
- Level 1 Epic(Business Goal)만 작성 요청
- 코드/테스트/파일 생성 금지, User Story/Task 분해 금지

**Assistant**
- Epic Title, Business Goal, Learning Goal, Problem Statement, Scope, Non-Scope, Success Criteria, Key Invariants, Traceability Rule, Level 2 후보 Story를 구조화해 제시

### Turn 2
**User**
- Level 2 User Journey 작성 요청
- 5개 Stage 고정 형식과 표 출력 요구

**Assistant**
- Persona, Journey Goal, Overview 표, Stage 1~5 상세, Story 매핑, Traceability Link 작성

### Turn 3
**User**
- Level 3 User Stories 작성 요청
- Boundary/Domain 분리, 테스트 가능한 Acceptance Criteria 요구

**Assistant**
- Story 1~5를 Layer별로 정리
- 각 Story별 AC, Protected Contract/Invariant, Future RED 방향 제시
- Traceability Matrix 작성

### Turn 4
**User**
- Level 4 Technical Scenario 작성 요청
- SC-DOM-SOL-001, SC-BND-VAL-001~003 상세 제공

**Assistant**
- 요청 형식에 맞춰 Scenario, 보호 Invariant/Contract, RED ID, Task Candidate, Decomposition Preview 정리

### Turn 5
**User**
- Level 5 Scenario Verification and Summary 요청
- 일관성/누락/책임 분리/분해 가능성/추적성 검증 요구

**Assistant**
- 적합성 점수와 상태 판정
- Epic->Journey, Journey->Story, Story->Scenario 검증표 작성
- Edge Case/Invariant/Dual-Track/Implementation 가능성 점검
- 누락 항목과 수정 권고사항 도출

### Turn 6
**User**
- `@.cursor/agents/report-backup-agent.md 리포트/백업` 요청

**Assistant**
- 에이전트 지침을 확인
- 다음 번호(06)로 Report/Prompting 백업 파일 쌍 생성

## 최종 결과 요약
- 이번 세션은 Level 1~5를 문서 중심으로 일관되게 확장했다.
- 최종 검증에서 핵심 흐름은 적합하나 일부 시나리오 보강 필요로 판단되었다.
- 본 파일과 짝 파일(Report)은 번호 `06`으로 동기화 저장되었다.
