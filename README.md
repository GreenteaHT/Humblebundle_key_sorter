# Humblebundle_key_sorter
 Tools to easily align and view Humble Bundle game keys


[Process]
1. Log-in 
   1. log-in page
   2. log-in (Using send_keys())
2. Scraping
   1. move to key page
   2. scraping
      1. Single game
         - platform
         - game-name(title)
            - name
            - steam-link(스팀에서 따로 긁어야함)
         - bundle-name
           - name
           - link
         - key
           - key serial
           - claimed
      2. Humble choice
         1. move to choice page
         2. scraping
            - platform
            - game-name(title)
               - name
               - steam-link(스팀에서 따로 긁어야함)
            - bundle-name
              - choice name
              - choice link
            - key
              - key serial
              - claimed
3. make csv file

[Work]
1. Log-in (Using selinium)

[Todo]
1. Log-in
- 인증 페이지가 뜨지않으면 다음 단계로 진행 될 수 있게 해야함

2. Scraping (Using request, bs4)


[확장]
- 확장 플랫폼 정하기
- 정렬하여 보여준 후 특정 목록만 csv로 출력
- 로그인 및 인증을 더 쉽게



         

