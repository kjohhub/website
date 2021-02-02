### Youtube Player



1. 개요
   
   - 이 사이트는 유튜브의 동영상을 검색하고 재생하며, 
   - 유튜브의 재생목록 기능과 시청기록 서비스를 제공한다.
   
   
   
2. 기능
   - 회원가입/ 탈퇴* - (한진용)
   - 로그인/로그아웃 * - (한진용)
   - 동영상 리스트 표시* - 검색결과, 재생목록, 시청기록
   - 동영상 검색*
   - 동영상 재생*
   - 재생 목록 추가*
   - 시청 기록 추가
   
   * 동영상 추가/ 삭제 (관리자) * - 관리자 페이지에서 음악 정보 추가 (엄정민)
     * title, 동영상 id, 업로드시간 에디트박스
     * 코드 붙여넣으면 정보를 크롤링해서 분류





역할분담...

* 오경진 : 메인 화면 - 유튜브 검색, 유튜브 재생, 재생 목록 추가
* 한진용 : 회원가입 화면, 로그인화면, 회원가입/ 탈퇴, 로그인/아웃
* 엄정민 : 관리자 화면, 동영상 정보 수집
* 공통 : 데이터베이스/ 화면 설계



3. 시나리오

   - 
   
   
   
4. 데이터베이스 설계

   * 회원 테이블 (memberTbl)

     | Name       | DataType    | Unsigned | Auto Inc | Not NULL | Default |
     | ---------- | ----------- | :------: | :------: | :------: | :-----: |
     | Id (PK)    | VARCHAR(16) |          |          |    Y     |         |
     | password   | VARCHAR(16) |          |          |    Y     |         |
     | name       | VARCHAR(16) |          |          |    Y     |         |
     | birth_date | DATE        |          |          |    Y     |         |
     | mobile     | VARCHAR(13) |          |          |          |  NULL   |
     | address    | VARCHAR(32) |          |          |          |  NULL   |

     

   * 동영상 테이블 (videoTbl)

     | Name        | DataType    | Unsigned | Auto Inc | Not NULL | Default |
     | ----------- | ----------- | :------: | :------: | :------: | :-----: |
     | Id (PK)     | VARCHAR(16) |          |          |    Y     |         |
     | title       | VARCHAR(64) |          |          |    Y     |         |
     | video_url   | VARCHAR(64) |          |          |    Y     |         |
     | image_url   | VARCHAR(64) |          |          |    Y     |         |
     | upload_time | VARCHAR(13) |          |          |    Y     |         |
   |             |             |          |          |          |         |
     

   

   * 재생 목록 테이블

     | Name          | DataType    | Unsigned | Auto Inc | Not NULL | Default |
     | ------------- | ----------- | :------: | :------: | :------: | :-----: |
     | index (PK)    | INT         |    Y     |    Y     |    Y     |         |
     | user_id (FK)  | VARCHAR(64) |          |          |    Y     |         |
     | video_id (FK) | VARCHAR(64) |          |          |    Y     |         |

     

   * 시청 기록 테이블

     | me            | DataType    | Unsigned | Auto Inc | Not NULL | Default |
     | ------------- | ----------- | :------: | :------: | :------: | :-----: |
     | index (PK)    | INT         |    Y     |    Y     |    Y     |         |
     | user_id (FK)  | VARCHAR(64) |          |          |    Y     |         |
     | video_id (FK) | VARCHAR(64) |          |          |    Y     |         |
     
     

5. 화면 설계

   * 로그인 화면
   * 회원가입 화면
   * 메인 화면
   * 관리자 화면



6. 동영상 데이터 수집

   * beautifulsoup로 youtube 영상정보 크롤링 : https://yuda.dev/106

     ```python
     https://onedrive.live.com/edit.aspx?resid=45F8937019156493!958&cid=83bb5d85-1810-4865-89d1-6ebfd23ec8dc&ithint=file%2cpptx&wdOrigin=OFFICECOM-WEB.START.MRU{'updated_time': '6개월 전', 
      'hits': '조회수 2,902,787회', 
      'title': 'Eminem - Phenomenal (Behind The Scenes)',
      'video_link': 'https://www.youtube.com/watch?v=NEGjmd_RzLU', 
      'img_link': 'https://i.ytimg.com/vi/NEGjmd_RzLU/hqdefault.jpg?custom=true&w=196&h=110&stc=true&jpg444=true&jpgq=90&sp=68&sigh=ZMXNqukOXArsvh0aKzMAzfzREUc',
      'play_time': '8:55'}
     ```

     
