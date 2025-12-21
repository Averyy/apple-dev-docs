# Investigating crashes for zombie objects

**Framework**: Xcode

Identify the signature of a zombie and investigate the cause of the crash.

#### Overview

Once an Objective-C or Swift object no longer has any strong references to it, the object is deallocated. Attempting to further send messages to the object as if it were still a valid object is a “use after free” issue, with the deallocated object still receiving messages called a .

##### Determine Whether a Crash Report Has Signs of a Zombie

The Objective-C runtime can’t message objects deallocated from memory, so crashes often occur in the [`objc_msgSend`](https://developer.apple.com/documentation/ObjectiveC/objc_msgSend), `objc_retain`, or `objc_release` functions. For example, a crash where the Objective-C runtime can’t send a message to the deallocated object looks like this:

```other
Thread 0 Crashed:
0   libobjc.A.dylib                   0x00000001a186d190 objc_msgSend + 16
1   Foundation                        0x00000001a1f31238 __NSThreadPerformPerform + 232
2   CoreFoundation                    0x00000001a1ac67e0 __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 24
```

Here’s another example, where the Objective-C runtime tries to release an object that’s already released:

```other
Thread 2 Crashed:
0   libobjc.A.dylib                 0x00007fff7478bd5c objc_release + 28
1   libobjc.A.dylib                 0x00007fff7478cc8c (anonymous namespace)::AutoreleasePoolPage::pop(void*) + 726
2   com.apple.CoreFoundation        0x00007fff485feee6 _CFAutoreleasePoolPop + 22
```

Another pattern that indicates a zombie object is a stack frame for an , which is a method that an object doesn’t implement. Often this kind of crash looks like code where an unexpected type of object is asked to do something it obviously can’t do, such as a number formatter class trying to play a sound. This is because the operating system reused memory that once held the deallocated object, and that memory now contains a different kind of object. A zombie identified by an unrecognized selector has a call stack with the [`doesNotRecognizeSelector(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/doesNotRecognizeSelector(_:)) method:

```other
Last Exception Backtrace:
0   CoreFoundation                    0x1bf596a48 __exceptionPreprocess + 220
1   libobjc.A.dylib                   0x1bf2bdfa4 objc_exception_throw + 55
2   CoreFoundation                    0x1bf49a5a8 -[NSObject+ 193960 (NSObject) doesNotRecognizeSelector:] + 139
```

If you reproduce a crash like this when debugging, the console logs additional information:

```other
Terminating app due to uncaught exception 'NSInvalidArgumentException',
    reason: '-[NSNumberFormatter playSound]: 
    unrecognized selector sent to instance 0x28360dac0'
```

In this example, a message was sent to a [`NumberFormatter`](https://developer.apple.com/documentation/Foundation/NumberFormatter) to perform the `playSound` selector, but [`NumberFormatter`](https://developer.apple.com/documentation/Foundation/NumberFormatter) doesn’t implement a method with that name, so the app crashed. An object was previously allocated at the same memory address as the current [`NumberFormatter`](https://developer.apple.com/documentation/Foundation/NumberFormatter) that did implement the `playSound` method, but that object was deallocated, and the unrelated [`NumberFormatter`](https://developer.apple.com/documentation/Foundation/NumberFormatter) object is now using the same memory address. The `playSound` selector is a clue for debugging. If you identify the class implementing the `playSound` selector, you can identify the code paths that call it and determine why the expected object deallocated too early.

##### Investigate the Source of the Zombie

In cases where a crash is caused by a zombie object, stack frames from the app may be in the backtrace, but not always. Even if no backtrace frames reference code in your app, your code contributed to the creation of the zombie, so investigate the source of the zombie with the Zombies instrument, as described in [`Finding zombies`](https://developer.apple.comhttps://help.apple.com/instruments/mac/current/#/dev612e6956). As you use the Zombies instrument, look for answers to the following questions, so you have the information needed to modify your code and remove the zombie:

- What was the type of the deallocated object, and what message was sent to it?
- When was the object actually deallocated?
- How was the object used after it was deallocated?

When modifying your code, pay attention to the expected lifetime of the objects involved. Consider which objects use strong references, and which objects use weak or unowned references, so that objects are deallocated only when no longer needed and not too soon. See [`ARC Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226-CH1-SW13) for information about Automatic Reference Counting in Objective-C, and the [`Swift documentation`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html) for information in Swift.

## See Also

- [Analyzing a crash report](analyzing-a-crash-report.md)
  Identify clues in a crash report that help you diagnose problems.
- [Investigating memory access crashes](investigating-memory-access-crashes.md)
  Identify crashes that arise from memory access issues, and investigate the cause of the crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/investigating-crashes-for-zombie-objects)*