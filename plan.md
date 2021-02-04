### Youtube 기반 음악 동영상 재생 서비스



1. 개요
   
   - 이 사이트는 **유튜브의** **음악 동영상**을 검색하고 재생하며, 
   - 회원의 **재생목록** 과 **시청기록** 서비스를 제공한다.
   
   
   
2. 기능
   - 회원가입/ 탈퇴* - (엄정민)
   - 로그인/로그아웃 * - (엄정민)
   - 동영상 리스트 표시* - 검색결과, 재생목록, 시청기록 (오경진)
   - 동영상 검색* (오경진)
   - 동영상 재생* (오경진)
   - 재생 목록 추가* (오경진)
   - 시청 기록 추가 (오경진)

   * 동영상 추가/ 삭제 (관리자) * - 관리자 페이지에서 음악 정보 추가 (엄정민)



3. 화면 설계

   * 로그인 화면 (엄정민)
   * 회원가입 화면 (엄정민)
   * 메인 화면 (오경진)
   * 동영상 관리 화면 (엄정민)
   
   
   
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
     | upload_time | VARCHAR(13) |          |          |          |         |

   

   * 재생 목록 테이블 (playlistTbl)

     | Name          | DataType    | Unsigned | Auto Inc | Not NULL | Default |
     | ------------- | ----------- | :------: | :------: | :------: | :-----: |
     | id (PK)       | INT         |    Y     |    Y     |    Y     |         |
     | user_id (FK)  | VARCHAR(64) |          |          |    Y     |         |
     | playlist_id   | INT         |    Y     |          |    Y     |    1    |
     | video_id (FK) | VARCHAR(64) |          |          |    Y     |         |

        > ex) 1 - userid#1 - 재생목록1 - videoid#10

     

   * 시청 기록 테이블 (historyTbl)

     | me            | DataType    | Unsigned | Auto Inc | Not NULL | Default |
     | ------------- | ----------- | :------: | :------: | :------: | :-----: |
     | id (PK)       | INT         |    Y     |    Y     |    Y     |         |
     | user_id (FK)  | VARCHAR(64) |          |          |    Y     |         |
     | video_id (FK) | VARCHAR(64) |          |          |    Y     |         |



5. View 및 Template 설계

   | URL                      | View              | Template    | 비고                                |
   | ------------------------ | ----------------- | ----------- | ----------------------------------- |
   | /youtube/                | index()           | index.html  | 메인화면을 보여줌                   |
   | /youtube/playlist/       | playlist()        | index.html  | 재생목록을 보여줌                   |
   | /youtube/playlist/insert | playlist_insert() |             | 재생목록에 동영상을 추가함          |
   | /youtube/history/        | history()         |             | 시청기록을 보여줌                   |
   | /youtube/history/insert  | history_insert()  |             | 시청기록에 동영상을 추가함          |
   | /youtube/login           | login()           | login.html  | 로그인화면을 보여줌                 |
   | /youtube/logout          | logout()          |             | 로그아웃함                          |
   | /youtube/manage          | manage()          | manage.html | 동영상관리화면을 보여줌             |
   | /youtube/manage/add      | add_video()       |             | 동영상 추가함                       |
   | /youtube/search/검색어   | search()          | index.html  | 동영상을 검색하고 결과목록을 보여줌 |
   | /admin/                  | (장고 기능)       |             |                                     |

   



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

     

7. 