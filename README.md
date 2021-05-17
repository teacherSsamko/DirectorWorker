# DirectorWorker
Director and Worker. using thread  
article: https://ssamko.tistory.com/69

## structure
![structure](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FwN7a9%2FbtqXyMd56Be%2Fq9S68P7hiaJbq8KV1cmss0%2Fimg.jpg)

## output sample
```bash
[24, 10, 2, 22, 28, 25, 16, 27, 6, 3, 1, 19, 8, 29, 12]
not to do...24
worker status
0 - None
0
assign 10 to worker 0
0...1/10
[2, 22, 28, 25, 16, 27, 6, 3, 1, 19, 8, 29, 12]
check worker
worker status in check done 0 - <Worker(Thread-1, started 123145387311104)>
worker status in check done 1 - None
worker status in check done 2 - None
worker status in check done 3 - None
worker status in check done 4 - None
worker status in check done 5 - None
0...2/10
0...3/10
0...4/10
worker status
0 - <Worker(Thread-1, started 123145387311104)>
worker status
1 - None
1
assign 2 to worker 1
1...1/2
[22, 28, 25, 16, 27, 6, 3, 1, 19, 8, 29, 12]
check worker
worker status in check done 0 - <Worker(Thread-1, started 123145387311104)>
worker status in check done 1 - <Worker(Thread-2, started 123145404100608)>
worker status in check done 2 - None
worker status in check done 3 - None
worker status in check done 4 - None
worker status in check done 5 - None
0...5/10
1...2/2
0...6/10
0...7/10
worker status
0 - <Worker(Thread-1, started 123145387311104)>
worker status
1 - <Worker(Thread-2, stopped 123145404100608)>
worker status
2 - None
2
assign 22 to worker 2
2...1/22
[28, 25, 16, 27, 6, 3, 1, 19, 8, 29, 12]
check worker
worker status in check done 0 - <Worker(Thread-1, started 123145387311104)>
worker status in check done 1 - <Worker(Thread-2, stopped 123145404100608)>
worker 1 finished
<Worker(Thread-2, stopped 123145404100608)>
worker status in check done 2 - <Worker(Thread-3, started 123145404100608)>
worker status in check done 3 - None
worker status in check done 4 - None
worker status in check done 5 - None
0...8/10
2...2/22
0...9/10
2...3/22
0...10/10
2...4/22
worker status
0 - <Worker(Thread-1, started 123145387311104)>
worker status
1 - None
1
assign 28 to worker 1
1...1/28
[25, 16, 27, 6, 3, 1, 19, 8, 29, 12]
check worker
worker status in check done 0 - <Worker(Thread-1, started 123145387311104)>
worker status in check done 1 - <Worker(Thread-4, started 123145420890112)>
worker status in check done 2 - <Worker(Thread-3, started 123145404100608)>
worker status in check done 3 - None
worker status in check done 4 - None
worker status in check done 5 - None
2...5/22
1...2/28
2...6/22
1...3/28
2...7/22
1...4/28
worker status
0 - <Worker(Thread-1, stopped 123145387311104)>
worker status
1 - <Worker(Thread-4, started 123145420890112)>
worker status
2 - <Worker(Thread-3, started 123145404100608)>
worker status
3 - None
3
assign 25 to worker 3
3...1/25
[16, 27, 6, 3, 1, 19, 8, 29, 12]
check worker
worker status in check done 0 - <Worker(Thread-1, stopped 123145387311104)>
worker 0 finished
<Worker(Thread-1, stopped 123145387311104)>
worker status in check done 1 - <Worker(Thread-4, started 123145420890112)>
worker status in check done 2 - <Worker(Thread-3, started 123145404100608)>
worker status in check done 3 - <Worker(Thread-5, started 123145387311104)>
worker status in check done 4 - None
worker status in check done 5 - None
2...8/22
1...5/28
3...2/25
2...9/22
1...6/28
3...3/25
2...10/22
1...7/28
3...4/25
worker status
0 - None
0
assign 16 to worker 0
0...1/16
[27, 6, 3, 1, 19, 8, 29, 12]
check worker
worker status in check done 0 - <Worker(Thread-6, started 123145437679616)>
worker status in check done 1 - <Worker(Thread-4, started 123145420890112)>
worker status in check done 2 - <Worker(Thread-3, started 123145404100608)>
worker status in check done 3 - <Worker(Thread-5, started 123145387311104)>
worker status in check done 4 - None
worker status in check done 5 - None
2...11/22
1...8/28
3...5/25
0...2/16
2...12/22
1...9/28
3...6/25
0...3/16
2...13/22
1...10/28
3...7/25
0...4/16
2...14/22
not to do...27
1...11/28
3...8/25
0...5/16
2...15/22
1...12/28
3...9/25
0...6/16
2...16/22
1...13/28
3...10/25
0...7/16
2...17/22
1...14/28
not to do...6
3...11/25
0...8/16
2...18/22
1...15/28
3...12/25
0...9/16
2...19/22
1...16/28
3...13/25
0...10/16
2...20/22
1...17/28
3...14/25
not to do...3
0...11/16
2...21/22
1...18/28
3...15/25
0...12/16
2...22/22
1...19/28
3...16/25
0...13/16
1...20/28
3...17/25
0...14/16
worker status
0 - <Worker(Thread-6, started 123145437679616)>
worker status
1 - <Worker(Thread-4, started 123145420890112)>
worker status
2 - <Worker(Thread-3, stopped 123145404100608)>
worker status
3 - <Worker(Thread-5, started 123145387311104)>
worker status
4 - None
4
assign 1 to worker 4
4...1/1
[19, 8, 29, 12]
check worker
worker status in check done 0 - <Worker(Thread-6, started 123145437679616)>
worker status in check done 1 - <Worker(Thread-4, started 123145420890112)>
worker status in check done 2 - <Worker(Thread-3, stopped 123145404100608)>
worker 2 finished
<Worker(Thread-3, stopped 123145404100608)>
worker status in check done 3 - <Worker(Thread-5, started 123145387311104)>
worker status in check done 4 - <Worker(Thread-7, started 123145404100608)>
worker status in check done 5 - None
1...21/28
3...18/25
0...15/16
1...22/28
3...19/25
0...16/16
1...23/28
3...20/25
1...24/28
worker status
0 - <Worker(Thread-6, stopped 123145437679616)>
worker status
1 - <Worker(Thread-4, started 123145420890112)>
worker status
2 - None
2
assign 19 to worker 2
2...1/19
[8, 29, 12]
check worker
worker status in check done 0 - <Worker(Thread-6, stopped 123145437679616)>
worker 0 finished
<Worker(Thread-6, stopped 123145437679616)>
worker status in check done 1 - <Worker(Thread-4, started 123145420890112)>
worker status in check done 2 - <Worker(Thread-8, started 123145404100608)>
worker status in check done 3 - <Worker(Thread-5, started 123145387311104)>
worker status in check done 4 - <Worker(Thread-7, stopped 123145404100608)>
worker 4 finished
<Worker(Thread-7, stopped 123145404100608)>
worker status in check done 5 - None
3...21/25
1...25/28
2...2/19
3...22/25
1...26/28
2...3/19
3...23/25
1...27/28
2...4/19
3...24/25
worker status
0 - None
0
assign 8 to worker 0
0...1/8
[29, 12]
check worker
worker status in check done 0 - <Worker(Thread-9, started 123145437679616)>
worker status in check done 1 - <Worker(Thread-4, started 123145420890112)>
worker status in check done 2 - <Worker(Thread-8, started 123145404100608)>
worker status in check done 3 - <Worker(Thread-5, started 123145387311104)>
worker status in check done 4 - None
worker status in check done 5 - None
1...28/28
2...5/19
3...25/25
0...2/8
2...6/19
0...3/8
2...7/19
0...4/8
worker status
0 - <Worker(Thread-9, started 123145437679616)>
worker status
1 - <Worker(Thread-4, stopped 123145420890112)>
worker status
2 - <Worker(Thread-8, started 123145404100608)>
worker status
3 - <Worker(Thread-5, stopped 123145387311104)>
worker status
4 - None
4
assign 29 to worker 4
4...1/29
[12]
check worker
worker status in check done 0 - <Worker(Thread-9, started 123145437679616)>
worker status in check done 1 - <Worker(Thread-4, stopped 123145420890112)>
worker 1 finished
<Worker(Thread-4, stopped 123145420890112)>
worker status in check done 2 - <Worker(Thread-8, started 123145404100608)>
worker status in check done 3 - <Worker(Thread-5, stopped 123145387311104)>
worker 3 finished
<Worker(Thread-5, stopped 123145387311104)>
worker status in check done 4 - <Worker(Thread-10, started 123145387311104)>
worker status in check done 5 - None
2...8/19
0...5/8
4...2/29
2...9/19
0...6/8
4...3/29
2...10/19
0...7/8
4...4/29
not to do...12
2...11/19
0...8/8
4...5/29
2...12/19
4...6/29
2...13/19
4...7/29
2...14/19
4...8/29
2...15/19
4...9/29
2...16/19
4...10/29
2...17/19
4...11/29
2...18/19
4...12/29
2...19/19
4...13/29
4...14/29
4...15/29
4...16/29
4...17/29
4...18/29
4...19/29
4...20/29
4...21/29
4...22/29
4...23/29
4...24/29
4...25/29
4...26/29
4...27/29
4...28/29
4...29/29
```
