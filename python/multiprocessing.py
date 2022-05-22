### threading 모듈 병렬처리 : 단일 프로세스 활용
### 스레드는 파일 읽고 쓰기 같은 작업에 유리(b/c GIL) -> CPU 연산 수행할 때 이득 X
import threading

threads = []
for num in range(12):
    t = threading.Thread(target = func, args = (num, ))
    # t.start : thread 독립적으로 실행
    t.start()
    threads.append(t)

# thread 종료
for t in threads:
    t.join()


### multoprocessing 모듈 병렬처리 : 멀티 프로세스 활용
### Pool
import multiprocessing as mp
num_cores = mp.cpu_counts() - 1

# 데이터프레임에 func연산을 병렬처리하는 함수
def parallel_dataframe(df, func, num_cores):
    df_split = np.array_split(df, num_cores)
    pool = mp.Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    # 작업 완료 후에 메모리를 계속 잡아먹는 것을 방지하기 위함
    pool.close()
    pool.join()
    return df


### multoprocessing 모듈 병렬처리 : 멀티 프로세스 활용
### Process
import multiprocessing as mp
num_cores = mp.cpu_counts() - 1

procs = []
for num in range(num_cores):
    p = mp.Process(target = func, args = (num, ))
    # t.start : thread 독립적으로 실행
    # 함수 입력인자가 여러 개일 때
    # mp.Process(target = func, args = (num, ), kwargs)
    # p.map(func, [(튜플로 여러 변수 처리)])
    p.start()
    procs.append(p)

# process 종료
for p in procs:
    p.join()


# 진행 바 보기
import parmap
num_cores = mp.cpu_counts() - 1

parmap.map(pm_pbar = True, pm_processes = num_cores)
