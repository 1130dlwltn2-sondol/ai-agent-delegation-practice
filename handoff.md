# 후속 작업 안내 (handoff)

## 파일 구조

```
ai-agent-delegation-practice/
├── README.md               # 책 소개 (위키독스 연동용)
├── TOC.md                  # 전체 목차
├── manuscript_full.md      # 전체 통합 원고 (편집용)
├── references.md           # 원문 출처 목록
├── qa_report.md            # QA 보고서
├── handoff.md              # 이 파일
├── 2026-10-10_topic3_sources.md     # 조사 노트 (근거)
├── 2026-10-10_topic3_curriculum.md  # 교재 설계서 (근거)
├── chapters/               # 장별 원고 01~08.md
├── pages/                  # 위키독스 페이지 순서 원고 17개
├── assets/                 # 표지 + 도식 5종
└── tools/                  # 이미지 생성 스크립트
```

## 위키독스 업로드 방법

다른 담당자가 이 저장소로 위키독스 책을 만듭니다. https://wikidocs.net/github/book/new/ 에서 제목 'AI 에이전트 업무 위임 입문', 기존 리포지토리 연결, 저장소 이름 'ai-agent-delegation-practice'로 생성합니다. pages/의 17개 파일이 목차 순서대로 올라갑니다.

## 최신 정보 갱신 지점

기능의 제공 범위가 바뀌면 다음 위치를 업데이트하세요.

- pages/04-preparation.md: 기능 확인 표 (쓸 수 있는 것/없는 것)
- pages/14-final-project.md: 기능 가용성 점검표
- pages/16-sources.md, references.md: 출처 접근일과 URL
- pages/17-closing.md: 업데이트 기준일

갱신 시 공식 발표 원문(G1, G2)을 다시 열어 날짜와 함께 기록하세요.

## 수정 방법

- 원고 수정: chapters/의 해당 장을 고친 뒤, pages/의 같은 장 파일에도 동일하게 반영하고, manuscript_full.md를 다시 조립합니다. 조립 명령:
  { for f in pages/01-cover.md pages/02-copyright.md pages/03-foreword.md pages/04-preparation.md pages/05-book-intro.md; do cat "$f"; echo; echo "---"; echo; done; for i in 1 2 3 4 5 6 7 8; do n=$(printf "%02d" $i); cat "chapters/$n.md"; echo; echo "---"; echo; done; for f in pages/14-final-project.md pages/15-glossary.md pages/16-sources.md pages/17-closing.md; do cat "$f"; echo; echo "---"; echo; done; } > manuscript_full.md
- 이미지 수정: tools/make_images.py를 고쳐 다시 실행합니다.

## 남은 작업

- book.pdf 제작: Bookforge 설치 후 practical 스타일로 빌드 (qa_report.md 미완료 항목 참고)
- 위키독스 붙여넣기 후 검수: 업로드 담당자가 수행
