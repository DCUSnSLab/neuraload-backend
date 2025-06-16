# NeuraLoad Data Directory

이 폴더는 컨테이너의 `/data` 디렉토리와 마운트되어:
- 로그 파일
- 설정 파일
- SSL 인증서
- 업로드된 파일들

이 저장됩니다.

## 구조
```
data/
├── log/           # 로그 파일들
├── config/        # 설정 파일들
├── ssl/           # SSL 인증서
└── public/        # 정적 파일들
    ├── upload/    # 업로드된 파일
    └── media/     # 미디어 파일
```
