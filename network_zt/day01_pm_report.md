## 6교시 · Wireshark 실행 · 첫 캡처 · 필터

### 문제 6-1 (Wireshark 실행하기)
- 고른 인터페이스 이름: `이더넷3`

### 문제 6-2 (캡처한 통신의 방향 읽기)
- Packets 숫자 · Protocol 열의 이름 세 개: `1027 · TLSv1.2, TCP, ARP`
- 숫자 → 443 과 443 → 숫자 가운데 어느 줄이 요청인가요? 그렇게 판단한 이유는 무엇인가요?: 
  - `숫자 → 443` (내 PC → 서버) 줄이 요청입니다. 출발지가 내 PC의 IP이고 목적지가 서버의 443(HTTPS) 포트이기 때문입니다.

### 문제 6-3 (패킷 하나를 층별로 펼치기)
- Source MAC · Source IP / Destination IP · Time to Live · Source Port / Destination Port · Flags:
  - `00:10:f3:a3:fc:96 · 172.64.155.209 / 192.168.100.74 · 56 · 443 / 57200 · (ACK)`
- 이 패킷은 내 PC 가 보낸 것인가요, 받은 것인가요? 어떻게 알았나요?: 
  - `서버에서 내 PC로 온 응답 패킷입니다. 출발지 IP가 내 PC(192.168.100.74)가 아닌 서버(172.64.155.209)이고, 목적지 IP가 내 PC이기 때문입니다.`

### 문제 6-4 (필터 결과와 뜻 비교하기)
- 전체 Packets · dns · udp · tcp.port == 443 의 Displayed:
  - `전체 1027 · dns(24) · udp(343) · tcp.port == 443(486)`
- 필터를 걸어도 Packets 는 그대로인데 Displayed 만 바뀌는 이유는 무엇인가요?: 
  - `표시 필터는 이미 캡처된 패킷을 삭제하는 것이 아니라, 조건에 맞는 패킷만 화면에 보여주도록 가리는 기능이기 때문입니다.`

## 7교시 · 내 연결을 잡아 보고서로 남기기

### 문제 7-1 (내 HTTP 연결 하나만 잡기)
- handshake.png 저장 · 세 줄 Info 의 신호 순서:
  - `handshake.png 저장 완료` (캡처 인터페이스: 이더넷 3 · 캡처 필터 tcp port 80 · 전체 11개)
  - ① No.1 `56921 → 80 [SYN] Seq=0` — 내 PC(192.168.100.74) → 서버(104.20.23.154) 「연결하자」
  - ② No.2 `80 → 56921 [SYN, ACK] Seq=0 Ack=1` — 서버 → 내 PC 「알았다, 나도 연결하자」
  - ③ No.3 `56921 → 80 [ACK] Seq=1 Ack=1` — 내 PC → 서버 「알았다」 → ESTABLISHED
  - 세 줄 모두 임시 포트 56921 을 써서 같은 연결임을 알 수 있습니다.

### 문제 7-2 (HTTP 요청과 연결 종료 찾기)
- 요청 줄의 Info · FIN 줄 수:
  - No.4 `GET /?q=network_day1 HTTP/1.1` (응답 No.7 `HTTP/1.1 200 OK (text/html)`) · FIN `2줄` (`http_get.png` 저장)
  - No.9 `56921 → 80 [FIN, ACK]` — 내 PC → 서버 「나는 다 보냈다」
  - No.10 `80 → 56921 [FIN, ACK]` — 서버 → 내 PC 「알았다 + 나도 다 보냈다」
  - 종료는 No.9 FIN → No.10 FIN,ACK → No.11 ACK 세 줄로 끝났습니다. 서버가 더 보낼 데이터가 없어서 「알았다(ACK)」와 「나도 다 보냈다(FIN)」를 한 패킷(No.10)에 같이 보냈기 때문입니다.
- 🔍 같은 요청을 HTTPS 로 보냈다면 어떻게 보였을까요?:
  - `Protocol 열에 TLS 로 표시되고 내용은 Application Data 로 암호화되어, GET 요청 줄과 검색어(network_day1)가 보이지 않았을 것입니다. IP 주소와 포트(443) 정도만 보입니다.`

### 문제 7-3 (보고서 완성하고 올리기)
- 깃허브 network_zt 폴더에 보고서와 사진 두 장이 보이나요: `예 — day01_pm_report.md, handshake.png, http_get.png 확인`