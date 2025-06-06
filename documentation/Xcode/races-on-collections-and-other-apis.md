# Races on collections and other APIs

**Framework**: Xcode

Detects when one thread accesses a mutable object while another thread is writing to it.

#### Overview

In Xcode 9 and later, the Thread Sanitizer detects unsafe thread accesses of [`Foundation`](https://developer.apple.com/documentation/Foundation) and [`Core Foundation`](https://developer.apple.com/documentation/CoreFoundation) framework APIs. This feature applies to the following collection types:

- [`NSMutableArray`](https://developer.apple.com/documentation/Foundation/NSMutableArray)
- [`NSMutableDictionary`](https://developer.apple.com/documentation/Foundation/NSMutableDictionary)
- [`CFMutableArray`](https://developer.apple.com/documentation/CoreFoundation/CFMutableArray)
- [`CFMutableDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFMutableDictionary)

##### Collection Race with a Mutable Array

In the following example, the code enumerates a mutable array in one thread while writing to the array from another without synchronizing access:

```swift
let array: NSMutableArray = []
var sum: Int = 0
// Executed on Thread #1
for value in array {
    sum += value as! Int
}
// Executed on Thread #2
array.add(42)
```

```objc
NSMutableArray *array = [NSMutableArray new];
NSInteger sum = 0;
// Executed on Thread #1
for (id value in array) {  
    sum += [value integerValue];
} 
// Executed on Thread #2
[array addObject:@42];
```

###### Solution

Use [`Dispatch`](https://developer.apple.com/documentation/Dispatch) APIs to coordinate access to `array` across multiple threads.

##### Collection Race with a Mutable Dictionary

In the following example, the code enumerates a mutable dictionary in one thread while writing to the dictionary from another without synchronizing access:

```swift
let dictionary: NSMutableDictionary = [:]
var sum: Int = 0
// Executed on Thread #1
for key in dictionary.keyEnumerator() {
    sum += dictionary[key] as! Int
}
// Executed on Thread #2
dictionary["forty-two"] = 42
```

```objc
NSMutableDictionary *dictionary = [NSMutableDictionary new];
NSInteger sum = 0;
// Executed on Thread #1
for (id key in dictionary) {
    sum += [dictionary[key] integerValue];
}
// Executed on Thread #2
dictionary[@"forty-two"] = @42;
```

###### Solution

Use [`Dispatch`](https://developer.apple.com/documentation/Dispatch) APIs to coordinate access to `dictionary` across multiple threads.

## See Also

- [Data races](data-races.md)
  Detects unsynchronized access to mutable state across multiple threads.
- [Swift access races](swift-access-races.md)
  Detects unsynchronized access to mutable state across multiple threads in Swift.
- [Uninitialized mutexes](uninitialized-mutexes.md)
  Detects when you use an uninitialized mutex.
- [Thread leaks](thread-leaks.md)
  Detects when you don’t close threads after use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/races-on-collections-and-other-apis)*