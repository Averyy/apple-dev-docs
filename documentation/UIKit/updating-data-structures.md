# Updating data structures

**Framework**: UIKit

Review your app’s data design and update it to conform with 64-bit architecture.

#### Overview

When you move your app to a 64-bit architecture, revisit the structures in your code. Examine C structures that have 32-bit representations. The 64-bit runtime aligns the contents of structures differently, so you need to pay particular attention to structures that store data to a file or transmit it across a network. These structures could be utilized by devices with architectures of different sizes.

Code that doesn’t use explicitly sized types can cause problems for other developers who review your code. Explicitly sized type declarations clarify data-size expectations and eliminate assumptions about architectures.

Inconsistency between type declarations in a function and their use in code cause inconsistent behaviors at runtime. You need to ensure that data you pass to functions or capture as a return value are the same type as the declared parameter type.

##### Align 64 Bit Integer Types

As a result of the increased size of the 64-bit architecture, the alignment of all 64-bit integer types in the runtime changes from 4 bytes to 8 bytes. Even if you specify each integer type explicitly, the two structures may still not be identical in both runtimes. This is important to know if you have data that was created by the 32-bit version of your app that you need to read in the 64-bit version.

In the following code, the alignment changes even though the fields are declared with explicit integer types.

```objc
struct bar {
    int32_t foo0;
    int32_t foo1;
    int32_t foo2;
    int64_t bar;
};
```

When this code is compiled with a 32-bit compiler, the field `bar` begins 12 bytes from the start of the structure. When the same code is compiled with a 64-bit compiler, the field `bar` begins 16 bytes from the start of the structure. Four bytes of padding are added after `foo2` so that `bar` is aligned to an 8-byte boundary.

![Alignment between 32-bit and 64-bit representations of the same structure.](https://docs-assets.developer.apple.com/published/9a3a801f885b898f629d35054e0f73fe/media-3109112%402x.png)

If you’re defining a new data structure, organize the elements with the largest alignment values first and the smallest values last. This organization eliminates the need for most padding bytes. If you’re working with an existing structure that includes misaligned 64-bit integers, you can use a pragma to force the proper alignment. The following code shows the same data structure, but here it’s forced to use the 32-bit alignment rules.

```objc
#pragma pack(4)
struct bar {
    int32_t foo0;
    int32_t foo1;
    int32_t foo2;
    int64_t bar;
};
#pragma options align=reset
```

Use this option sparingly because there’s a performance penalty for misaligned accesses. You might use this option, for example, to maintain backward compatibility with data structures that were deployed in the 32-bit version of your app.

##### Use Explicit Integer Data Types

The C99 standard provides built-in data types that are guaranteed to be a specific size, regardless of the underlying hardware architecture. The following table lists the C99 types and defined ranges of values for each.

| Type | Defined range |
| --- | --- |
| `int16_t` | -32,768 to 32,767 |
| `int32_t` | -2,147,483,648 to 2,147,483,647 |
| `int64_t` | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 |
| `uint8_t` | 0 to 255 |
| `uint16_t` | 0 to 65,535 |
| `uint32_t` | 0 to 4,294,967,295 |
| `uint64_t` | 0 to 18,446,744,073,709,551,615 |

Avoid types such as `short`, `int`, or `unsigned int`. Instead, use types that are guaranteed to be a specific size, regardless of the underlying hardware architecture.

Choosing a fixed-width type also avoids allocating a variable whose range is much larger than you need, and saves memory.

##### Keep Data Types Consistent

Inconsistent use of data types in your code can truncate results of computation and provide incorrect results. Even though the compiler warns you of many problems that result from inconsistent data types, it’s also useful to see a few variations of these patterns so that you can recognize them in your code.

When calling a function, always match the variable that receives the results to the function’s return type. If the return type is a larger integer than the receiving variable, the value is truncated. The following code shows a simple pattern that exhibits this problem.

```objc
long PerformCalculation(void);

int  x = PerformCalculation(); // Incorrect.

long y = PerformCalculation(); // Correct.
```

The `PerformCalculation` function returns a long integer. In the 32-bit runtime, both `int` and `long` are 32 bits, so the assignment to an `int` type works, even though the code is incorrect. In the 64-bit runtime, the upper 32 bits of the result are lost when the assignment is made. Instead, the result should be assigned to a long integer; this approach works consistently in both runtimes.

The same problem occurs when you pass in a value as a parameter. Here, the input parameter is truncated when executed in the 64-bit runtime.

```objc
int PerformAnotherCalculation(int input);

long i = LONG_MAX;

int x = PerformCalculation(i);
```

In the following code, the return value is also truncated in the 64-bit runtime, because the value returned exceeds the range of the function’s return type.

```objc
int ReturnMax()
{
    return LONG_MAX;
}
```

All of these examples result from code that assumes that `int` and `long` are identical. The ANSI C standard doesn’t make this assumption, and it’s explicitly incorrect when working in the 64-bit runtime. By default, if you modernized your project as described in [`Updating your app from 32-bit to 64-bit architecture`](updating-your-app-from-32-bit-to-64-bit-architecture.md), the `-Wshorten-64-to-32` compiler option was automatically enabled, so the compiler automatically warns you about many cases where a value is truncated. If you didn’t modernize your project, you should explicitly enable that compiler option. Optionally, you may want to include the `-Wconversion` option, which is more verbose, but finds more potential errors.

##### Choose an Appropriate Data Type for Enumerated Values

In the LLVM compiler, enumerated types can define the size of the enumeration, so some enumerated types may be larger than you expect. The solution, as in all other cases, is to make no assumptions about a data type’s size. Instead, assign any enumerated values to a variable with the proper data type.

##### Look for Common Type Conversion Problems

The `NSInteger` type is used throughout the system for declaring numeric types. It’s a 32-bit integer in the 32-bit runtime and a 64-bit integer in the 64-bit runtime. Never make the assumption that an `NSInteger` type is the same size as an `int` type. Here are a few cases in your code to look for:

- Converting to or from an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object.
- Encoding and decoding data using the [`NSCoder`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/MacOSX/WhatsNewInOSX/Articles/MacOSX10_11.html#//apple_ref/doc/uid/TP40016227-SW42) class. In particular, if you encode an `NSInteger` on a 64-bit device and later decode it on a 32-bit device, the decode method throws an exception if the value exceeds the range of a 32-bit integer. You may want to use an explicit integer type instead.
- Working with constants defined in the framework as `NSInteger`. Of particular note is the `NSNotFound` constant. In the 64-bit runtime, its value is larger than the maximum range of an `int` type, so truncating its value often causes errors in your app.

Don’t assume the size of `CGFloat`. As a result of the conversion, the `CGFloat` type changes to a 64-bit floating-point number. As with the `NSInteger` type, you can’t assume that `CGFloat` is a `float` or a `double`, so use it consistently. The following code shows an example that uses Core Foundation to create a `CFNumber:`

```objc
// Incorrect.
CGFloat value = 200.0;
CFNumberCreate(kCFAllocatorDefault, kCFNumberFloatType, &value);

// Correct.
CGFloat value = 200.0;
CFNumberCreate(kCFAllocatorDefault, kCFNumberCGFloatType, &value);
```

The first part of the code assumes that a `CGFloat` is the same size as a `float`, which is incorrect. The second part of the code correctly specifies `kCFNumberCGFloatType` as the type to create.

## See Also

- [Auditing pointer usage](auditing-pointer-usage.md)
  Ensure that the pointers in your code are safe for the 64-bit runtime.
- [Managing functions and function pointers](managing-functions-and-function-pointers.md)
  Ensure that your code correctly handles functions, function pointers, and Objective-C messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/updating-data-structures)*