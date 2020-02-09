// The entry file of your WebAssembly module.

export function add(a: i32, b: i32): i32 {
  return a + b;
}

NativeMath.seedRandom(1234);

export function fib(num : i64) : i64 {
  var a : i32 = 1;
  var b :i32 = 0;
  var temp:i32;

  while (num >= 0){
    temp = a;
    a = a + b;
    b = temp;
    num--;
  }
  return b;
}

// Box-Mueller
export function normal() : f64 {
		var urand = Math.random();
		var vrand = Math.random();
    return Math.sqrt( -2.0*Math.log( urand ) ) * Math.cos( 2.0*Math.PI*vrand );
}