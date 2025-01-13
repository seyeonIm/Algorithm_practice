# 베스트 노래 두개를 앨범 하나로 출시, 수록 노래 반환 
# 수록 기준: 인기 장르 < 많이 재생 < 낮은 고유번호
def solution(genres, plays):
    answer = []
    
    plays_by_genre = {}
    integrated_gp = {}
    genre_songs = {}
    
    # 장르 별 재생횟수 총합 딕셔너리화, 장르 별 각 재생횟수 딕셔너리화
    for i, (genre,play) in enumerate(zip(genres,plays)):
        if genre not in plays_by_genre:
            plays_by_genre[genre] = play
            integrated_gp[genre] = [(play,i)]
        else:
            plays_by_genre[genre] += play
            integrated_gp[genre].append((play,i))
    
    print(plays_by_genre)
    print("int",integrated_gp)
    sorted_genres = sorted(plays_by_genre, key = lambda x: plays_by_genre[x], reverse = True)
    # sorted_genres = sorted(plays_by_genre, key=lambda x: plays_by_genre[x], reverse=True)
    
    print(sorted_genres)
    
    for genre in sorted_genres:
        oneGenre_playlist = sorted(integrated_gp[genre], key = lambda x : (x[0], -x[1]), reverse = True)
        print(oneGenre_playlist[:2])  
        # answer.append(oneGenre_playlist[0][1])
        # answer.append(oneGenre_playlist[1][1])
        for song in oneGenre_playlist[:2]:
            answer.append(song[1])
    
    # print(answer)
    print("one",oneGenre_playlist)
    return answer



# 문제를 풀려면 뭘 알아내야할까?
# genre_total_plays
# 이 딕셔너리는 각 장르의 총 재생 횟수를 저장합니다:
# python
# genre_total_plays = {
#     "pop": 650,      # 500 + 150
#     "classic": 1400, # 600 + 800
#     "jazz": 1100
# }
# genre_songs
# 이 딕셔너리는 각 장르별로 노래의 인덱스와 재생 횟수를 튜플 형태로 저장합니다:
# python
# genre_songs = {
#     "pop": [(0, 500), (2, 150)],
#     "classic": [(1, 600), (3, 800)],
#     "jazz": [(4, 1100)]
# }
