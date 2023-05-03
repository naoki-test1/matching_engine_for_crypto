

Architecture
- 

- Time complexity for critical operations are as.

       Add – O(log M) for the first order at a limit, O(1) for all others
       Cancel – O(1)
       Execute – O(1)
       Where M is price Limit and << N

- Data processing i-e store transaction and history logs operation are carried out on separate thread[s].The number of thread[s] are configurable and benchmark for 4 threads are given in thread_result.

- Data between Main Thread and Worker Thread[s] is shared using Configurable Queues.

- Batched Data is inserted in Database and batch size can be configured for different operations.

Installation
- 
Install Dependencies
       make deps-install
              OR
       pip install -r requirements.txt
Install Application
       make install

Test
- 
       #All Tests
       make run-tests
       # Single
       python -m unittest test.testOrder

BenchMark
- 
       make run-benchmarks
       
Running
- 
Large order file for benchmarking or testing.

       script_runner.py < ./sample_data/largeOrder600K.txt
Multi-threaded script for inserting data in persistence layer.

       threaded_script.py < sample_data/largeOrder600K.txt

Input Data Format
- 
Limit Orderbook scripts expect the following input format i-e [in a DAT or txt file]

       Bid or Sell => B or S
       Order ID => Unique or autoincrementing Integer
       Price => Integer
       Quantity => Integer Sample Order format in a file can be
       
Sample Order => S,0,23,1000
