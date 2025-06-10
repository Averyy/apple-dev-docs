# Improving build efficiency with good coding practices

**Framework**: Xcode

Shorten compile times by reducing the number of symbols your code exports and by giving the compiler the explicit information it needs.

#### Overview

Reducing build times by even a few seconds can have a significant impact over the course of development. Xcode does everything possible to build your code as fast as possible. It parallelizes build tasks and takes advantage of all available resources to output a finished product. However, you can help Xcode by making sure you’re not creating unnecessary work for the compiler.

Over the years, Xcode’s compiler has introduced optimizations to speed up compile times. Most of these optimizations are automatic, but some require you to make small changes to your code. In addition, projects that support both Objective-C code to Swift may require additional optimizations to ensure fast compile times.

> **Note**: You can also optimize build times through project-level changes. For more information on optimizing build times, see [`Improving the speed of incremental builds`](improving-the-speed-of-incremental-builds.md).

##### Include Framework Names in Import Statements

When you import headers into your source files, always include the name of the parent framework or library in your import statement. In C-based code, importing headers usually copies the contents of the header file into your source. When you include the framework name, the compiler has the option to use module maps to import the headers, which significantly reduces importation time. With module maps, the compiler loads and processes the framework’s header files once, and caches the resulting symbol information on disk. When you import the same framework from another source file, the compiler reuses the cached data, eliminating the need to again read and preprocess the header files.

Include framework names for both system frameworks and any custom frameworks you create in your projects. The following example shows import statements for both a system and custom framework, both of which have module maps. The last import statement continues to load and process the header file contents directly, rather than using an available module map.

```occ
// Imports the framework’s module map
#import <UIKit/UIKit.h>
#import <PetKit/PetKit.h>     // Custom framework

// Performs a textual inclusion of the header file.
#import "MyHeader.h"

```

For information about how to add a module map to your custom frameworks, see Create Module Maps for Custom Frameworks and Libraries.

##### Minimize the Number of Symbols You Share Between Swift and Objective C

When you mix Swift and Objective-C code in your project, your Swift code might need to know about portions of your Objective-C code, and vice versa. The compiler handles this exchange of symbol information using two special header files:

- The Objective-C bridging header determines which Objective-C symbols you make available to your Swift code.
- The compiler-generated Swift header is a list of all public Swift symbols you can use in your Objective-C code.

Reducing the size of both header files reduces the compiler’s workload and improves compilation times. A smaller file size means the compiler can process the headers more quickly. It also means faster symbol lookup times when compiling source files.

When configuring the contents of your Objective-C bridging header, include only the headers and symbols you actually reference from your Swift source. If your Swift code uses only part of an Objective-C class, move the symbols your Swift code doesn’t use into categories in your implementation file or in an internal-only header file.

The following figure illustrates how you might separate the symbols you use externally from those your class uses internally. The `MyViewController.h` header contains only the subset of symbols you reference publicly from your Swift code. The `MyViewController-Internal.h` header includes the remaining symbols in category extensions on your class. Include both headers in your Objective-C implementation file, but include only the public header in your Objective-C bridging file.

![An illustration of one header file that contains public symbols and a separate header file that contains symbols intended only for internal use. ](https://docs-assets.developer.apple.com/published/ea53988c2ab83ed6edae8b073984c8d1/improving-build-efficiency-with-good-coding-practices-1%402x.png)

The compiler makes all of your public Swift symbols available to your Objective-C code automatically using a generated header. To minimize the size of this generated header, update your Swift code in the following ways:

- Mark internal methods and properties of your Swift classes as `private`. The presence of that keyword prevents the inclusion of the symbol in the generated header file.
- Choose block-based APIs over function-based APIs. Blocks are part of your implementation, and don’t generate public symbol information.
- Support the most-recent version of the Swift language. Swift 3 and earlier automatically infer Objective-C type information for most symbols, which increases the size of the generated header. Later versions of Swift perform automatic type inference in fewer situations, reducing the overall size of the header.

##### Provide the Swift Compiler with Explicit Type Information

The Swift compiler is capable of inferring the type of a variable from the value you assign to it. For simple values, the inference process is quick. For example, if you assign the value `0.0` to a property, the compiler can quickly determine that the type is a floating-point number. However, if you assign a complex value to a variable, the compiler must perform extra work to compute any type information.

Consider the following structure, in which the `bigNumber` property has no explicit type information. To determine the type of that property, the Swift compiler must evaluate the results of the [`reduce(_:_:)`](https://developer.apple.com/documentation/Swift/Array/reduce(_:_:)) function, which takes a nontrivial amount of time.

```swift
struct ContrivedExample {
   var bigNumber = [4, 3, 2].reduce(1) {
      soFar, next in
      pow(next, soFar)
   }
}
```

Instead of letting the compiler determine the type, the best practice is to provide the type explicitly as shown in the example below. Providing explicit type information reduces the work the compiler must do, and also allows it to do more error checking.

```swift
struct ContrivedExample {
   var bigNumber : Double = [4, 3, 2].reduce(1) {
      soFar, next in
      pow(next, soFar)
   }
}
```

##### Define Delegate Methods in Explicit Protocols

Delegates are a standard design pattern on Apple platforms, and provide a useful way to communicate between objects. Although delegation enables communication between arbitrary objects, always provide explicit type information for your delegate objects.

Consider the following example of a delegate declared as an optional object of any type. Although this declaration is perfectly legal, it actually creates more work for the compiler. The compiler must assume that any object in your project or referenced frameworks contains the function, and so it searches your entire project to make sure that function exists somewhere.

```swift
weak var delegate: AnyObject?
func reportSuccess() {
   delegate?.myOperationDidSucceed(self)
}
```

Instead of using any object, a better approach is to supply specific type information. Typically, you specify the type information using a delegate protocol, as shown in the example below. An explicit protocol helps the compiler find the method more quickly. It also allows the compiler to perform additional type checking for objects you assign to the `delegate` property.

```swift
weak var delegate: MyOperationDelegate?
func reportSuccess() {
   delegate?.myOperationDidSucceed(self)
}

protocol MyOperationDelegate {
   func myOperationDidSucceed(_ operation: MyOperation)
}
```

##### Simplify Complex Swift Expressions

The Swift language allows you to write code in very expressive ways, but make sure your code doesn’t affect compile times. Consider an example of a function that uses the `reduce` function to sum a set of values. If you pass `nil` for all the arguments, the function returns `nil`, but if you pass one or more arguments, it sums the sum of those arguments. The function takes advantage of a Swift feature, in which the compiler uses the one-line expression in the closure to determine the return type of that closure.

```swift
func sumNonOptional(i: Int?, j: Int?, k: Int?) -> Int? {
   return [i, j, k].reduce(0) {
      soFar, next in
      soFar != nil && next != nil ? soFar! + next! : (soFar != nil ? soFar! : (next != nil ? next! : nil))
   }
}
```

Although this function represents legal Swift syntax, the one-line closure makes the code hard to read and harder for the compiler to evaluate. In fact, the compiler aborts with an error that states it cannot type-check the expression in a reasonable amount of time. The one-line closure is also unnecessary. The definition of the [`reduce(_:_:)`](https://developer.apple.com/documentation/Swift/Array/reduce(_:_:)) function causes it to return the same type you pass in, which in this case is an optional integer.

Rather than use such a complex expression, it’s better to create something simpler and more readable. The following code offers the same behavior as the single-line closure version, but is easier to read and compiles quickly.

```swift
func sumNonOptional(i: Int?, j: Int?, k: Int?) -> Int? {
   return [i, j, k].reduce(0) {
      soFar, next in
      if let soFar = soFar {
         if let next = next { return soFar + next }
         return soFar
      } else {
         return next
      }
   }
}
```

## See Also

- [Configuring your project to use mergeable libraries](configuring-your-project-to-use-mergeable-libraries.md)
  Use mergeable dynamic libraries to get app launch times similar to static linking in release builds, without losing dynamically linked build times in debug builds.
- [Improving the speed of incremental builds](improving-the-speed-of-incremental-builds.md)
  Tell the Xcode build system about your project’s target-related dependencies, and reduce the compiler workload during each build cycle.
- [Building your project with explicit module dependencies](building-your-project-with-explicit-module-dependencies.md)
  Reduce compile times by eliminating unnecessary module variants using the Xcode build system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/improving-build-efficiency-with-good-coding-practices)*