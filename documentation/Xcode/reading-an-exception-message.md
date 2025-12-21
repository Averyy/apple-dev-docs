# Reading an exception message

**Framework**: Xcode

Understand and address the common reasons apps crash.

#### Overview

Frameworks detect common errors associated with using their APIs and raise exceptions when they occur. If your app doesn’t handle those errors, for example by calling [`NSSetUncaughtExceptionHandler(_:)`](https://developer.apple.com/documentation/Foundation/NSSetUncaughtExceptionHandler(_:)) to install an exception handler, then it crashes. The operating system records a crash report that contains information about the app’s state at the time of the crash.

The following sections each describe common mistakes in using framework APIs and the exception messages that appear in your app’s crash reports when it encounters these cases. In each case, the exception thread trace in the crash report shows the location in your code where your app crashed. For more information, see [`Analyzing a crash report`](analyzing-a-crash-report.md).

##### Address a Crash Caused By Adding a Null Object to a Collection

`Foundation`‘s collection classes like [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), its mutable subclass [`NSMutableArray`](https://developer.apple.com/documentation/Foundation/NSMutableArray), and `CoreFoundation` counterparts like [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) can’t contain `nil` as a value. Additionally, dictionary collections — [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSMutableDictionary`](https://developer.apple.com/documentation/Foundation/NSMutableDictionary), [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) — can’t contain `nil` as a key. If your app adds `nil` to a mutable collection, it crashes, and an exception message like this example is included in the crash report:

```None
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '*** -[__NSArrayM insertObject:atIndex:]: object cannot be nil'
```

If you need to add an object to a `Foundation` or `CoreFoundation` collection class that represents a lack of any valid value, use [`null`](https://developer.apple.com/documentation/Foundation/NSNull/null) or [`kCFNull`](https://developer.apple.com/documentation/CoreFoundation/kCFNull). Otherwise, test an object’s value before you add it to a collection and don’t add it if the object is `nil`.

##### Address a Crash Caused By Using a Null Object in Apis That Require Non Null Parameters

Many APIs expect their parameters to be non-`nil` and throw exceptions if they receive `nil`. For example, [`addAttribute(_:value:range:)`](https://developer.apple.com/documentation/Foundation/NSMutableAttributedString/addAttribute(_:value:range:)) requires both its `name` and `value` to be non-`nil`. If your app adds a `nil` attribute to an attributed string, it crashes, and an exception message like this example is included in the crash report:

```None
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: 'NSConcreteMutableAttributedString addAttribute:value:range:: nil value'
```

Determine an appropriate non-`nil` value to use instead; otherwise, avoid setting the attribute.

APIs that require non-`nil` parameters include nullability designations, and you can add nullability designations to your own methods, blocks, and functions. The compiler detects when you use an object that’s potentially `nil` in situations where a non-`nil` object is required, and emits a warning. For more information, see [`Designating Nullability in Objective-C APIs`](https://developer.apple.com/documentation/Swift/designating-nullability-in-objective-c-apis).

##### Address a Crash Caused By Sending an Unrecognized Selector to a Class or Object

You often send messages to Objective-C classes and objects by writing the method name into your source code; for example, you send [`addAttribute(_:value:range:)`](https://developer.apple.com/documentation/Foundation/NSMutableAttributedString/addAttribute(_:value:range:)) by typing `[myAttributedString addAttribute:aName value:aValue range:aRange];`. There are situations where you construct a method name — also known as a  — dynamically and send that to the class or object. A common example is setting the name of a controller method as an action in a storyboard file. If the object or class receiving the message doesn’t respond to the selector and can’t forward it to another object, your app crashes and an exception message like this example is included in the crash report:

```None
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[__NSCFBoolean insertObject:atIndex:]: unrecognized selector sent to instance 0x1e75db6c0'
```

Check that the method selector is spelled correctly, including colons to indicate each of the arguments. Verify that the class of the receiving object implements the requested method or forwards it to an object that implements it.

##### Address a Crash Caused By Inserting Replacing or Deleting an Object in an Immutable Collection or Sequence

Each of the common `Foundation` collections has an immutable class, for example, [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), and a corresponding mutable subclass, for example, [`NSMutableArray`](https://developer.apple.com/documentation/Foundation/NSMutableArray). These Objective-C classes are interchangeable with the corresponding `CoreFoundation` types [`CFArray`](https://developer.apple.com/documentation/CoreFoundation/CFArray) and [`CFMutableArray`](https://developer.apple.com/documentation/CoreFoundation/CFMutableArray). It’s an error to try to change the contents of an immutable collection, for example, by appending an object. If your app tries to change the contents of an immutable collection, it crashes and an exception message like this example is included in the crash report:

```None
*** Terminating app due to uncaught exception 'NSInternalInconsistencyException', reason: '-[__NSCFArray insertObject:atIndex:]: mutating method sent to immutable object'
```

If you need to modify a collection that you share with other code, the source of the original collection needs to initialize a mutable collection. If you need to make changes to a local copy of the original collection, which remains immutable, use `-mutableCopy` to create a local, mutable version. Otherwise, remove the code that modifies the collection.

> **Note**: A common cause of this exception is incorrectly interchanging `Foundation` and `CoreFoundation` collection classes, for example, casting a `CFArrayRef` to Objective-C using `(__bridge NSMutableArray *)`. When you use toll-free bridging to interchange `Foundation` and `CoreFoundation` collection classes, ensure that the bridged types of Objective-C variables match the types of their `CoreFoundation` counterparts, including their mutability.

##### Address a Crash Caused By Using an Index Range or Position Thats Out of Bounds

APIs that take a parameter indicating the position of an object or other data in an ordered collection or a sequence raise an exception if that position is outside the containing collection. APIs that take a parameter indicating a range of values in a sequence raise an exception if either the start or end of the range is outside the containing collection.

> **Note**:  The special value [`NSNotFound`](https://developer.apple.com/documentation/Foundation/NSNotFound-4qp9h) isn’t meant to be used as a position in a collection or sequence and will cause an out-of-range exception if you use it this way in your code.

If your app tries to access the content of a collection or sequence outside of its range, it crashes and an exception message like this example is included in the crash report:

```None
*** Terminating app due to uncaught exception 'NSRangeException', reason: '*** -[__NSArrayM objectAtIndex:]: index 12 beyond bounds [0 .. 0]'
```

In the special case of requesting an object at a particular index in an empty array, the exception message is similar to this example:

```None
*** Terminating app due to uncaught exception 'NSRangeException', reason: '*** -[__NSArray0 objectAtIndex:]: index 12 beyond bounds for empty array'
```

Check that your app is using an up-to-date value for the collection’s size, and that the code that calculates the position or range is correct.

##### Address a Crash Caused By Requesting a Range That Overflows the Integer Type

The [`NSRange`](https://developer.apple.com/documentation/Foundation/NSRange-c.struct) structure uses the same type ([`NSUInteger`](https://developer.apple.com/documentation/ObjectiveC/NSUInteger)) for both its location and its length, which is also the type that collection classes use to represent indexes into the collection. It’s possible to create a range where the end of the range is beyond the values that can be represented as indexes into the collection that’s using the range. When a collection or sequence detects this case, your app crashes and an exception message like this example is included in the crash report:

```None
*** Terminating app due to uncaught exception 'NSRangeException', reason: '*** -[NSConcreteMutableData subdataWithRange:]: range {20, 18446744073709551605} causes integer overflow'
```

Check that your app is using an up-to-date value for the collection’s size, and that the code that calculates the range is correct.

##### Address a Crash Caused By Incorrectly Initializing a Dictionary

When you initialize an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) or [`NSMutableDictionary`](https://developer.apple.com/documentation/Foundation/NSMutableDictionary) using the initializer method [`init(objects:forKeys:)`](https://developer.apple.com/documentation/Foundation/NSDictionary/init(objects:forKeys:)), you have to supply an equal number of keys and objects. If you supply arrays with different lengths, your app crashes and an exception message like this example is included in the crash report:

```None
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '*** -[NSDictionary initWithObjects:forKeys:]: count of objects (1) differs from count of keys (2)'
```

Check your code to determine which array you pass — the keys or the objects — is incorrect.

##### Address a Crash Caused By Attempting to Encode or Decode an Object That Isnt Codable

To serialize or deserialize an object using [`NSCoder`](https://developer.apple.com/documentation/Foundation/NSCoder), whether to store it in a file, or send it to another process or over the network, the object must conform to [`NSCoding`](https://developer.apple.com/documentation/Foundation/NSCoding). If your app attempts to encode or decode an object that doesn’t conform to `NSCoding`, it crashes and an exception message like this example is included in the crash report:

```None
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[MyClass encodeWithCoder:]: unrecognized selector sent to instance 0x600002090040'
```

Replace the object with one that conforms to `NSCoding`, or add `NSCoding` conformance to the object’s class or to a category on that class.

> **Note**:  While collection classes such as `NSArray` and `NSDictionary` are codable, each object in the collection must also conform to `NSCoding` for a collection to encode itself correctly.

## See Also

- [Addressing crashes from Swift runtime errors](addressing-crashes-from-swift-runtime-errors.md)
  Identify the signs of a Swift runtime error, and address the crashes runtime errors cause.
- [Addressing language exception crashes](addressing-language-exception-crashes.md)
  Identify the signs of a language exception, and address the crashes caused by uncaught language exceptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reading-an-exception-message)*