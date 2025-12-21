# Adopting type-aware memory allocation

**Framework**: Xcode

Reduce the opportunities to treat pointers as data in your code.

#### Overview

The compiler supports type-aware memory allocations, which track the data types you allocate memory for, and returns pointers to memory in different regions for different data types. The typed allocator generates a descriptor for any type of data structure you allocate in your code, for example, a C `struct` or a C++ `class`. When you allocate memory for storing a particular type of data structure, the compiler computes the type’s descriptor and returns memory from a zone dedicated to containing memory with that descriptor.

Because the system records that the memory zone containing the pointer is associated with the specified type, it can isolate allocations for memory regions that contain pointers from allocations for pure-data regions.

When you enable the type-aware memory allocator, the compiler automatically rewrites calls to `malloc`, `calloc`, `realloc`, `posix_memalign`, related functions, and the C++ `new` operator, to use type-aware equivalents.

##### Enable the Type Aware Memory Allocator for Your Target

Xcode automatically configures your target to use the type-aware memory allocator, in addition to other hardening settings, when you add the Enhanced Security capability. For more information, see [`Enabling enhanced security for your app`](enabling-enhanced-security-for-your-app.md).

To enable the type-aware memory allocator without adding the Enhanced Security capability, in your target:

- Add the [`Hardened Heap`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.hardened-heap) entitlement with the value `YES`
- Set the `CLANG_ENABLE_C_TYPED_ALLOCATOR_SUPPORT` build setting with the value `YES`
- Set the `CLANG_ENABLE_CPLUSPLUS_TYPED_ALLOCATOR_SUPPORT` build setting with the value to `YES`

##### Make Type Aware Memory Allocations

You need to call the type-aware version of memory-allocation functions anywhere you use runtime information to determine type before allocating memory. For example, if your app includes a runtime library for a programming language that uses runtime information to determine the type of a pointer. To call the type-aware version of memory-allocation functions yourself, prefix the function name with `malloc_type_`. For example, `malloc` becomes `malloc_type_malloc`.

The `malloc_type_` functions take an additional parameter compared with the regular allocator functions, that’s the type descriptor of the type you allocate. Calculate the type descriptor for a given type by constructing a `malloc_type_descriptor_v0_t` that describes the type, and reading its `type_id` member value.

If you use `union` types, avoid designing a type that uses the same location for either a pointer or for data, as the typed allocator can’t protect that memory.

##### Create Type Aware Allocator Wrappers

If your project includes wrapper functions that call the system’s memory-allocation functions, consider whether you can remove the wrappers and call the memory-allocation functions directly, and benefit from the compiler’s automatic rewrites to use typed allocators. If you can’t remove your wrapper functions, write type-aware variants of the wrapper functions and use the `_MALLOC_TYPED` macro to annotate your existing wrapper functions with references to their type-aware variants. The macro takes two parameters:

- The name of the type-aware wrapper function
- The index, in the original function’s argument list, of the argument developers use to pass the allocation’s size (the first argument is at position `1`)

For example:

```c
#if defined(_MALLOC_TYPE_ENABLED) && _MALLOC_TYPE_ENABLED

// Declare the type-aware variant of your wrapper function.
void *my_malloc_typed(size_t size, malloc_type_id_t type_id);

// Declare your wrapper function, and annotate it with a reference to the type-aware variant.
void *my_malloc(size_t size) _MALLOC_TYPED(my_malloc_typed, 1);

#else

// Declare your wrapper function without any annotation.
void *my_malloc(size_t size);

#endif
```

In your wrapper function’s type-aware variant, return a pointer to memory that you allocate using the `malloc_type_` library function variants:

```c
void *my_malloc_typed(size_t size, malloc_type_id_t type_id) {
  // Implement the custom logic for your wrapper function.

  return malloc_type_malloc(size, type_id);
}
```

## See Also

- [Verifying the origin of your XCFrameworks](verifying-the-origin-of-your-xcframeworks.md)
  Discover who signed a framework, and take action when that changes.
- [Enabling enhanced security for your app](enabling-enhanced-security-for-your-app.md)
  Detect out-of-bounds memory access, use of freed memory, and other potential vulnerabilities.
- [Creating enhanced security helper extensions](creating-enhanced-security-helper-extensions.md)
  Reduce opportunities for an attacker to target your app through its extensions.
- [Conforming to Mach IPC security restrictions](conforming-to-mach-ipc-security-restrictions.md)
  Avoid crashes and potentially insecure situations associated with Mach messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/adopting-type-aware-memory-allocation)*