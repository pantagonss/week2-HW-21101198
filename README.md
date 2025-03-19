# Cartoonify Image - OpenCV 기반 만화 효과 변환
이 프로젝트는 OpenCV를 사용하여 이미지를 만화 스타일로 변환하는 알고리즘을 구현합니다.  
Adaptive Thresholding 및 Bilateral Filtering을 활용하여 선명한 윤곽선과 부드러운 색상을 유지하는 것이 목표입니다.

---

## 데모

### ✅ 잘 표현되는 이미지 예제
알고리즘이 효과적으로 적용된 이미지 사례입니다.

![Good Example](./good_example.jpg)

특징:
- 선명한 윤곽선과 적절한 색감 유지
- 배경과 객체가 명확하게 분리됨

### ❌ 잘 표현되지 않는 이미지 예제
알고리즘이 비효율적으로 동작하는 이미지 사례입니다.

![Bad Example](./bad_example.jpg)

문제점:
- 너무 어두운 이미지에서 윤곽선이 제대로 추출되지 않음
- 복잡한 텍스처가 있는 이미지에서 지나치게 강한 엣지 효과 발생

---

## 한계점 및 개선 방향

### 한계점
1. **복잡한 배경 문제**  
   - 배경이 복잡하면 윤곽선이 과하게 강조되어 원치 않는 노이즈가 발생할 수 있음.
  
2. **색 보존 한계**  
   - Bilateral 필터를 사용하지만 원본 이미지의 색감이 일정 부분 손실될 수 있음.
  
3. **해상도 의존성**  
   - 낮은 해상도의 이미지는 엣지 검출 과정에서 디테일이 뭉개질 가능성이 있음.

### 개선 방향
- 딥러닝 기반의 스타일 변환 모델 (예: CartoonGAN) 적용
- 이미지 텍스처에 따라 다르게 적용할 수 있는 적응형 필터링 기법 도입
- 더욱 자연스러운 색 변환을 위한 추가적인 보정 과정 추가

---

## 실행 방법
```bash
python cartoonify.py

<img width="960" alt="image" src="https://github.com/user-attachments/assets/fe4ca40c-8a9b-49ab-ac46-a486f525fba8" />

<img width="960" alt="image" src="https://github.com/user-attachments/assets/9bfc97c8-76ed-4cf0-b5e3-78900ea29b36" />
