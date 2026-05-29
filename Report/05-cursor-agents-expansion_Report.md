# Cursor Agents Expansion Report

## 작업 배경/목표

- Cursor Subagent 구성을 확장하기 위해 역할별 에이전트 템플릿을 정리하고 실제 에이전트 파일을 생성했다.
- 코드 리뷰어를 시작점으로 시스템 최적화, UX, PM, 백엔드, 프런트엔드, QA, AI 통합, 보고서/백업 자동화 역할까지 범위를 확대했다.

## 수행 내용

1. `code-reviewer` 에이전트 생성 및 지침 작성
2. 시스템 최적화/UX 에이전트 프롬프트 초안 제안
3. 사용자 요청에 따라 다음 에이전트 파일 생성
   - `system-optimization-engineer`
   - `ux-specialist`
   - `product-manager`
   - `backend-developer`
   - `frontend-developer`
   - `qa-engineer`
   - `ai-integration-specialist`
   - `report-backup-agent`
4. `report-backup-agent`에 보고서/프롬프트 번호 동기화 규칙 및 루틴 절차 명시

## 생성/수정 파일 목록

- `.cursor/agents/code-reviewer.md`
- `.cursor/agents/system-optimization-engineer.md`
- `.cursor/agents/ux-specialist.md`
- `.cursor/agents/product-manager.md`
- `.cursor/agents/backend-developer.md`
- `.cursor/agents/frontend-developer.md`
- `.cursor/agents/qa-engineer.md`
- `.cursor/agents/ai-integration-specialist.md`
- `.cursor/agents/report-backup-agent.md`
- `Report/05-cursor-agents-expansion_Report.md`
- `Prompting/05-cursor-agents-expansion_Prompt.md`

## 결과

- `.cursor/agents`에 역할 기반 에이전트 구성이 완료되어 재사용 가능한 멀티에이전트 운영 기반을 확보했다.
- 모든 신규 에이전트는 공통 frontmatter(`name`, `description`, `model: inherit`)를 포함하도록 정렬했다.
- 보고서/백업 자동화 에이전트를 통해 세션 종료 시 기록 루틴을 표준화할 수 있게 되었다.

## 검증

- `.cursor/agents` 디렉터리에서 생성 파일 목록 확인 완료
- `Report`/`Prompting` 다음 번호가 `05`인지 확인 후 동일 번호로 문서 생성 완료

## 남은 이슈 및 다음 액션

- 각 에이전트별 출력 템플릿(체크리스트/리포트 형식) 표준화 여부 결정
- `report-backup-agent`를 실제 세션에서 반복 실행해 번호 규칙 일관성 점검
