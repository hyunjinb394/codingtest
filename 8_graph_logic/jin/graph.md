## 그래프 알고리즘

1. 그래프 표현방법 (V : 노드 수 , E: 간선 수 )
   
    a. 인접 행렬
    * 2차원 배열로 표현하는 방법
    * 간선이 존재하면 1, 없으면 0
    * **메모리** : 가능한 모든 노드 쌍을 표현해야하기 때문에 O(V^2)가 필요, 즉 노드 수가 증가할 수록 필요한 메모리 공간이 빠르게 증가
    * **시간 복잡도** : 특정 노드 A에서 노드 B로 간선이 존재하는지 배열로 접근해서 확인하므로 O(1)의 시간이 걸림

    b. 인접 리스트
    * 각 노드마다 리스트를 만들어서 그 노드와 연결된 다른 노드를 기록하는 방법
    * **메모리** : 간선 개수만큼의 메모리 공간이 필요,  모든 간선을 기록하기 때문에 O(E)가 필요
    * **시간복잡도** : 특정 노드 A에서 다른 노드 B로 간선이 존재하는지 확인하기 위해선 노드 A의 리스트를 전부 탐색해야함. 최악의 경우 모든 리스트를 확인해야하기 때문에 O(V)의 시간이 걸림

2. 언제나 예시로 이해하자

    a. 인접 행렬 
         
         a b c
       a 0 1 1  
       b 1 0 1   
       c 1 1 0

    * 3 * 3의 행렬, 즉 9개의 공간이 필요
    * a -> b로 가는 간선은 1 , 바로 확인 가능
    * 메모리 공간이 많이 필요하지만, 특정 간선의 존재 여부를 빠르게 파악 가능

    b. 인접 리스트  

        a : b, c   
        b : a, c  
        c : a, b 

    * 필요한 공간은 O(E), 간선의 수에 비례  
    * 메모리 공간을 절약할 수 있지만, 간선의 존재 여부를 파악하는데 인접 행렬보다 많은 시간이 걸림


## 위상 정렬 (Topological Sort)

1. 개념   

    a. 방향 그래프 : 방향을 가지는 간선을 가짐
    b. 선행 관계 : 방향 그래프에서 간선으로 선행 관계가 그려짐
    c. 위상 정렬 :  노드들을 간선의 방향성을 가지고 일렬로 나열하는 알고리즘, 선행 관계가 있기 때문에 정렬이 가능

2. 특징

    a. 사이클이 없는 방향 그래프여야 함
    b. 선후 관계 순서가 있어야 함

3. 알고리즘 flow   
    a. 각 노드들의 간선 수 계산
    b. 진입 차수가 0인 노드를 큐에 추가
    c. 선택된 노드의 이웃 노드의 진입 차수를 1씩 감소
    d. 진입 차수가 0이 된 노드를 선택하고 큐에 추가
    e. 위 과정 반복으로 모든 노드를 방문
    f. 큐에서 노드를 꺼내서 큐가 빌때까지 반복하면 모든 노드의 순서가 결정됨




    