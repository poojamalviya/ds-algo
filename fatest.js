// var calc = function() {
//     var pointer = 0;
//     function add(val) {
//         pointer += val;
//     }
//     return {
//         adder: function(val) {
//             add(val);
//         },
//         value: function() {
//             return pointer;
//         }
//     }
// }

// var cal1 = calc();
// cal1.adder(10);
// var cal2 = calc();
// console.log(cal1.value());
// console.log(cal2.value());


// function alter( a, b ) {
//     a=10;
//     b.a = 10;
// }

// var a = 2;
// var b = {a: 2, b: 3};
// alter(a,b);
// console.log(a);
// console.log(b.a);


// for (var i = 0; i < 4; i++) {
//     setTimeout(function(loc_i) { 
//         return function() { alert(loc_i); } 
//     }(i), 1000+i);
// }

// for (let i = 0; i < 4; i++) {
//     setTimeout(function(loc_i) { 
//         return function() { alert(loc_i); } 
//     }(i), 1000+i);
// }


// for (var i = 0; i < 4; i++) {
//     setTimeout(function(){ alert(i); }, 1000);
// }


// for (let i = 0; i < 4; i++) {
//     setTimeout(function(){ console.log(i); }, 1000);
// }

// function outer_func()  
// { 
//     var x = 0;
//     function inner_func(val)  
//     { 
//         return function()  
//         { 
//             x += val
//             return x;
//         } 
//     } 
//     var arr = []; 
//     for (var i = 0; i < 4; i++)  
//     { 
//         arr[i] = inner_func(i); 
//     } 
//     return arr; 
// } 
// var arr_func = outer_func(); 
// console.log(arr_func[0]()); 
// console.log(arr_func[1]()); 
// console.log(arr_func[2]()); 
// console.log(arr_func[3]());


// var express = require('express')
// var app = express()
// const port = 5000

// app.use((req, res, next) => {
//     console.log(req.method, req.path);
// })

// app.get('/', function (req, res) {
//     res.send('Hello')
// })

// app.listen(port, () => console.log(`App listening on port ${port}!`))

// var obj = function() {}

// obj.prototype.scp = function() {
//     console.log(this === "window" ? "window" : "obj");
// };

// var obj1 = new obj();

// var scp = obj1.scp;

// obj1.scp();
// scp();

// Promise.resolve('res1')
//        .then(Promise.resolve('res2'))
//        .then(Promise.resolve('res3'))
//        .then(function (result){
//                  console.log(result);
//      });

// function myFunction(name){
//     return () => {
//         console.log(`Next tick ${name}`);
//     }
//  }
 
//  function myTimeout(delay, message){
//     setTimeout(() => {
//         console.log(`Timeout is ${message}`);
//     }, delay);
//  }

// process.nextTick(myFunction('First'));
// myTimeout(0,'After first');
// process.nextTick(myFunction('Second'));
// myTimeout(0,'After second'); 

// var spawn = require('child_process').spawn;

// if (process.argv[2] === 'child') {
//     count += 1
//     console.log('child', count)
//     var net = require('net');
//     var pipe = new net.Socket({ fd: 3});
//     pipe.write('KILL');
//     console.log('Writing');
// } else {
//     var count = 0
//     var child = spawn(process.execPath, [__filename, 'child'], {
//         stdio: [null, null, null, 'pipe']
//     })
//     child.stdio[3].on('data', function(data) {
//         if (data.toString() === 'KILL') {
//             console.log('RIP');
//                 child.kill();
//             }
//     })
//     console.log('parent', count);
//     child.stdout.pipe(process.stdout);
// }


// let userOne = {
//     firstName: "Rahul",
//     sayHi: () => this.firstName,
//   };
//   console.log(userOne.sayHi());
  
//   let userTwo = {
//     firstName: "Rajendra",
//     sayHi()  { return this.firstName; },
//   };
//   console.log(userTwo.sayHi());


// const EventEmitter = require('events');

// class TestEmitter extends EventEmitter {}
// const testEmitter = new TestEmitter();

// testEmitter.once('newListener', (event, listener) => {
//   if (event === 'event') {
//     testEmitter.on('event', () => {
//       console.log('Steve');
//     });
//   }
// });

// testEmitter.on('event', () => {
//   console.log('Mark');
// });

// testEmitter.emit('event');


// const buf1 = Buffer.from('ABC');
// const buf2 = Buffer.from('BCD');
// const buf3 = Buffer.from('ABCD');

// console.log([buf1, buf2, buf3].sort(Buffer.compare).map(x => x.toString()));
  

func_arr = []
for(let i = 0; i < 3; i++) {
    func_arr[i] = function(result) {
        console.log("func" + i + " started with " + result);
        return new Promise(function (resolve) {
            setTimeout(function () {
                console.log("func" + i + " ended");
                resolve("result of func" + i);
            }, 1000);
        });
    }
}

// func_arr[0]().then(function (result) {
//     return func_arr[1](result);
// }).then(func_arr[2]);

func_arr[0]().then(func_arr[1])
    .then(func_arr[2]);