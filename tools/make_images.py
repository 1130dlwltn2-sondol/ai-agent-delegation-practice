#!/usr/bin/env python3
"""표지 및 도식 이미지 생성 - AI 에이전트 업무 위임 입문"""
from PIL import Image, ImageDraw, ImageFont

BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

CREAM = (253, 246, 236)
INK = (43, 43, 43)
CORAL = (231, 111, 81)
TEAL = (42, 157, 143)
YELLOW = (244, 162, 97)
SOFT_BLUE = (168, 218, 220)
LIGHT_CORAL = (250, 220, 210)
WHITE = (255, 255, 255)

def font(path, size):
    return ImageFont.truetype(path, size)

def center_text(d, y, text, f, fill, W):
    bbox = d.textbbox((0, 0), text, font=f)
    d.text(((W - (bbox[2] - bbox[0])) / 2, y), text, font=f, fill=fill)

def rounded(d, xy, r, fill, outline=None, width=1):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

# ============ 표지 1000x1300 ============
W, H = 1000, 1300
img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

# 상단 장식 바
d.rectangle([0, 0, W, 14], fill=CORAL)
d.rectangle([0, 14, W, 22], fill=YELLOW)

# 텍스트 영역 (상단)
center_text(d, 90, "AI 입문 시리즈", font(BOLD, 44), CORAL, W)
center_text(d, 180, "AI 에이전트", font(BOLD, 120), INK, W)
center_text(d, 320, "업무 위임 입문", font(BOLD, 120), INK, W)
center_text(d, 500, "Gemini 업무 에이전트 발표로 배우는", font(REG, 44), (90, 90, 90), W)
center_text(d, 560, "목표·권한·검수 설계", font(BOLD, 54), TEAL, W)

# 구분선
d.line([120, 660, 880, 660], fill=(210, 200, 185), width=3)

# 하단 일러스트 영역 (친근한 애니메이션풍)
# 배경 원들
d.ellipse([80, 720, 300, 940], fill=LIGHT_CORAL)
d.ellipse([700, 700, 940, 940], fill=(215, 240, 235))
d.ellipse([400, 980, 620, 1200], fill=(255, 235, 200))

# 문서 (왼쪽)
rounded(d, [130, 780, 360, 1080], 24, WHITE, outline=(200, 190, 175), width=3)
for i, yy in enumerate([830, 890, 950, 1010]):
    d.ellipse([160, yy, 190, yy + 30], fill=TEAL if i < 3 else (200, 200, 200))
    d.rounded_rectangle([210, yy + 5, 330, yy + 25], radius=10, fill=(235, 230, 220) if i < 3 else (245, 242, 235))

# 로봇 에이전트 캐릭터 (중앙)
# 몸통
rounded(d, [430, 800, 600, 1020], 60, SOFT_BLUE, outline=TEAL, width=4)
# 머리
rounded(d, [445, 700, 585, 830], 55, WHITE, outline=TEAL, width=4)
# 안테나
d.line([515, 700, 515, 660], fill=TEAL, width=6)
d.ellipse([500, 635, 530, 665], fill=CORAL)
# 눈 (웃는 눈)
d.ellipse([475, 745, 505, 775], fill=INK)
d.ellipse([525, 745, 555, 775], fill=INK)
# 입 (미소)
d.arc([490, 770, 540, 810], start=10, end=170, fill=INK, width=5)
# 팔 (체크 들고)
d.rounded_rectangle([400, 860, 445, 950], radius=20, fill=SOFT_BLUE, outline=TEAL, width=3)
d.rounded_rectangle([585, 860, 630, 950], radius=20, fill=SOFT_BLUE, outline=TEAL, width=3)
# 가슴 체크 배지
d.ellipse([495, 880, 535, 920], fill=CORAL)
d.line([502, 900, 510, 908], fill=WHITE, width=5)
d.line([510, 908, 524, 892], fill=WHITE, width=5)

# 목표 과녁 (오른쪽)
for r, col in [(110, CORAL), (85, WHITE), (60, YELLOW), (35, CORAL)]:
    d.ellipse([770 - r, 880 - r, 770 + r, 880 + r], fill=col, outline=CORAL if col == WHITE else None, width=3 if col == WHITE else 1)
d.ellipse([762, 872, 778, 888], fill=CORAL)

# 화살표 (문서 -> 로봇 -> 과녁)
d.line([360, 930, 400, 930], fill=TEAL, width=6)
d.polygon([400, 915, 400, 945, 425, 930], fill=TEAL)
d.line([630, 930, 660, 930], fill=CORAL, width=6)
d.polygon([660, 915, 660, 945, 685, 930], fill=CORAL)

# 하단 텍스트
center_text(d, 1150, "저자 이준수", font(BOLD, 40), INK, W)
center_text(d, 1205, "업데이트 기준일 2026-10-10", font(REG, 32), (120, 120, 120), W)

img.save("/home/hatch/workspace/ai-agent-delegation-practice/assets/cover.png")
print("cover ok", img.size)

# ============ 도식 공통 ============
def diagram_base(w, h, title):
    im = Image.new("RGB", (w, h), WHITE)
    dr = ImageDraw.Draw(im)
    dr.rectangle([0, 0, w, 90], fill=CREAM)
    center_text(dr, 22, title, font(BOLD, 40), INK, w)
    dr.line([0, 92, w, 92], fill=(210, 200, 185), width=2)
    return im, dr

# 1. 위임 수준 도식
im, dr = diagram_base(900, 560, "위임 수준 3단계 (모식도)")
levels = [("단순 질문", "답만 받는다", TEAL, 130), ("다단계 위임", "목표를 주고 실행은 맡긴다", YELLOW, 270), ("사람 승인 필수", "발송·결제·삭제 전 확인", CORAL, 410)]
for name, desc, col, y in levels:
    rounded(dr, [60, y, 840, y + 110], 20, WHITE, outline=col, width=4)
    dr.ellipse([90, y + 35, 130, y + 75], fill=col)
    dr.text([160, y + 18], name, font=font(BOLD, 38), fill=INK)
    dr.text([160, y + 62], desc, font=font(REG, 30), fill=(100, 100, 100))
dr.text([60, 530], "실제 제품 화면이 아닙니다.", font=font(REG, 22), fill=(150, 150, 150))
im.save("/home/hatch/workspace/ai-agent-delegation-practice/assets/diagram-delegation-levels.png")
print("delegation ok")

# 2. 권한 매트릭스 도식
im, dr = diagram_base(900, 560, "권한 매트릭스 예시 (모식도)")
headers = ["도구", "읽기", "쓰기", "삭제"]
rows = [["매출 엑셀", "허용", "금지", "금지"], ["보고서 문서", "허용", "허용", "금지"], ["팀 공유 폴더", "허용", "보류", "금지"], ["메일함", "금지", "금지", "금지"]]
cw = [300, 170, 170, 170]
x0 = 45
for j, htxt in enumerate(headers):
    dr.rectangle([x0 + sum(cw[:j]), 120, x0 + sum(cw[:j+1]), 175], fill=CREAM, outline=(200, 190, 175))
    dr.text([x0 + sum(cw[:j]) + 20, 130], htxt, font=font(BOLD, 32), fill=INK)
for i, row in enumerate(rows):
    y = 175 + i * 85
    for j, cell in enumerate(row):
        fill = WHITE
        tcol = INK
        if cell == "허용":
            fill = (220, 245, 240); tcol = TEAL
        elif cell == "금지":
            fill = (250, 225, 218); tcol = CORAL
        elif cell == "보류":
            fill = (255, 243, 220); tcol = (180, 130, 40)
        dr.rectangle([x0 + sum(cw[:j]), y, x0 + sum(cw[:j+1]), y + 85], fill=fill, outline=(200, 190, 175))
        dr.text([x0 + sum(cw[:j]) + 20, y + 22], cell, font=font(BOLD, 30), fill=tcol)
dr.text([45, 525], "실제 제품 화면이 아닙니다.", font=font(REG, 22), fill=(150, 150, 150))
im.save("/home/hatch/workspace/ai-agent-delegation-practice/assets/diagram-permission-matrix.png")
print("permission ok")

# 3. 승인 게이트 흐름도
im, dr = diagram_base(900, 640, "승인 게이트 흐름도 (모식도)")
steps = ["자료 수집", "집계·표 작성", "초안 작성", "사람 검수", "공유"]
x = 60
for i, s in enumerate(steps):
    col = CORAL if s == "사람 검수" else (TEAL if i < 3 else YELLOW)
    rounded(dr, [x, 180, x + 130, 300], 20, WHITE, outline=col, width=4)
    dr.text([x + 12, 218], s, font=font(BOLD, 26), fill=INK)
    if i < 4:
        dr.line([x + 130, 240, x + 160, 240], fill=(120, 120, 120), width=4)
        dr.polygon([x + 160, 228, x + 160, 252, x + 178, 240], fill=(120, 120, 120))
    x += 160
# 승인 게이트 강조
rounded(dr, [60, 360, 840, 480], 20, (255, 243, 230), outline=CORAL, width=3)
dr.text([90, 380], "승인 게이트: 공유(외부 행동) 전에는 반드시 사람 확인", font=font(BOLD, 30), fill=CORAL)
dr.text([90, 425], "예외 분기(자료 없음·합계 불일치·검수 반려)는 사람에게 보고 후 중단이 기본값", font=font(REG, 26), fill=(100, 100, 100))
dr.text([60, 600], "실제 제품 화면이 아닙니다.", font=font(REG, 22), fill=(150, 150, 150))
im.save("/home/hatch/workspace/ai-agent-delegation-practice/assets/diagram-approval-flow.png")
print("approval ok")

# 4. 감사 로그 구조
im, dr = diagram_base(900, 560, "감사 로그 항목 (모식도)")
items = ["시각: 언제 실행했는가", "정체성: 어떤 에이전트가 했는가", "행동: 무엇을 했는가", "대상: 어디에 했는가", "권한: 어떤 권한으로 했는가", "승인자: 누가 승인했는가", "결과: 성공했는가"]
y = 120
for it in items:
    rounded(dr, [60, y, 840, y + 52], 12, CREAM, outline=(200, 190, 175), width=2)
    dr.text([85, y + 10], it, font=font(REG, 28), fill=INK)
    y += 58
dr.text([60, 530], "실제 제품 화면이 아닙니다.", font=font(REG, 22), fill=(150, 150, 150))
im.save("/home/hatch/workspace/ai-agent-delegation-practice/assets/diagram-audit-log.png")
print("audit ok")

# 5. 비용 통제
im, dr = diagram_base(900, 560, "비용 통제 구조 (모식도)")
rounded(dr, [60, 130, 410, 280], 20, WHITE, outline=TEAL, width=4)
dr.text([90, 150], "Smart Routing", font=font(BOLD, 34), fill=TEAL)
dr.text([90, 200], "작업에 맞는 모델 선택", font=font(REG, 28), fill=(100, 100, 100))
rounded(dr, [490, 130, 840, 280], 20, WHITE, outline=CORAL, width=4)
dr.text([520, 150], "지출 상한", font=font(BOLD, 34), fill=CORAL)
dr.text([520, 200], "상한 도달 시 에이전트 중단", font=font(REG, 28), fill=(100, 100, 100))
rounded(dr, [60, 330, 840, 470], 20, CREAM, outline=(200, 190, 175), width=2)
dr.text([90, 350], "운영 기록: 회차·소요 시간·가상 비용·성공 여부를 매번 기록", font=font(BOLD, 30), fill=INK)
dr.text([90, 400], "모든 수치는 가상이며 실제 요금이 아닙니다.", font=font(REG, 26), fill=(120, 120, 120))
dr.text([60, 525], "실제 제품 화면이 아닙니다.", font=font(REG, 22), fill=(150, 150, 150))
im.save("/home/hatch/workspace/ai-agent-delegation-practice/assets/diagram-cost-control.png")
print("cost ok")
print("ALL DONE")
