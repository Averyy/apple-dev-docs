# Embedding nonstandard code structures in a bundle

**Framework**: Xcode

Use code that’s structured in a nonstandard way while avoiding code signing and distribution problems.

#### Overview

All apps — and many non-app software products on the Mac, like plug-ins — are packaged in a bundle structure.  When creating a bundle, place content in the correct location.  Placing content in a nonstandard location can cause code signing and distribution problems.  For more on this, see [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle).

In some cases you need to work with nonstandard code structures, that is, code whose structure doesn’t match the standard bundle structure for your platform.  For example, you might be building a Mac app and want to embed an open source language runtime in it.  If the on-disk layout of this runtime doesn’t follow the rules in [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle), you run the risk of code signing and distribution problems.

The best way to resolve this conundrum is to rebuild the code to match your target platform’s bundle structure.  However, this isn’t always feasible:

- It requires extensive knowledge of the code’s build system.  If you’re not already familiar with that, you may spend a lot of time gaining that knowledge.
- It only works if the product is open source.

Fortunately there’s another way.  This document walks you through an example of how to embed a nonstandard code structure into your bundle without having to rebuild all the code.  This example is for the Mac but the basic techniques work on all Apple platforms.

> ❗ **Important**: This is just an example.  It’s likely that the code you’re using will have a structure that’s different from this example.  Adapt the techniques shown here to your specific situation.

This is just an example.  It’s likely that the code you’re using will have a structure that’s different from this example.  Adapt the techniques shown here to your specific situation.

##### Separate Read Only and Readwrite Content

A bundle is a read-only structure.  All Apple platforms except the Mac enforce this requirement at runtime.  On iOS, for example, any attempt to modify your app’s bundle at runtime will fail with an error.  The Mac may or may not enforce this requirement at runtime, depending on the context, but modifying your app’s bundle isn’t supported because it breaks the seal on the app’s code signature.

Code structures with their origins on other platforms are not always compatible with this requirement.  For example, the Python runtime writes bytecode files in the same directory in as the original Python source file.  If, say, you have a file called `WaffleVarnish.py`, the runtime may write a file called `WaffleVarnish.pyc` (or `WaffleVarnish.pyo`) into that directory.  This causes two problems:

- If the platform blocks this write, you miss out on the performance benefits of these bytecode files.
- If the platform does not block this write, the write breaks the seal on your app’s code signature.

If the code you’re using works this way, find a way to separate its read-only content, which you can safely place in your bundle, and its read/write content, which you can’t.  The details are specific to the code in question, but this often involves setting a command-line argument or an environment variable that points to a writable location, for example, in the Library directory.

##### Investigate Dynamic Library Linkage

Imagine you’re building a Mac app to varnish waffles and want to use the fabulous open source libWaffleVarnish code.  Its build system outputs a directory structure like this:

```None
libWaffleVarnish/
  bin/
    wafflevarnish
  etc/
    wafflevarnish.config
  lib/
    libVarnish.dylib
    libWaffle.dylib
```

The `wafflevarnish` tool depends on both dynamic libraries.  The `libVarnish.dylib` library depends on `libWaffle.dylib`.  The `wafflevarnish` tool also reads the `wafflevarnish.config` configuration file.

The good news here is that libWaffleVarnish is structured in a way that makes it easy to relocate.  The `wafflevarnish` tool sets up the rpath context via an executable relative path that leads to the `lib` directory:

```None
% otool -l libWaffleVarnish/bin/wafflevarnish | grep -B 1 -A 2 LC_RPATH 
Load command 15
          cmd LC_RPATH
      cmdsize 40
         path @executable_path/../lib …
```

And both `wafflevarnish` and `libVarnish.dylib` reference their dynamic library dependencies with rpath-relative references:

```None
% otool -L "libWaffleVarnish/bin/wafflevarnish"
…
    @rpath/libVarnish.dylib …
    @rpath/libWaffle.dylib …
    …
% otool -L "libWaffleVarnish/lib/libVarnish.dylib"
…
    @rpath/libVarnish.dylib …
    @rpath/libWaffle.dylib …
    …
% otool -L "libWaffleVarnish/lib/libWaffle.dylib"
…
    @rpath/libWaffle.dylib …
    …
```

For more information on the rpath mechanism, see the `dyld` man page.  If you’re unfamiliar with reading man pages, see [`Reading UNIX Manual Pages`](https://developer.apple.com/documentation/os/reading-unix-manual-pages).

With this setup it’s easy to place this tool and its libraries in your bundle with a minimum amount of disruption.  If the code you’re using is built this way, skip forward to [`Place content in the correct location within the bundle`](embedding-nonstandard-code-structures-in-a-bundle#Place-content-in-the-correct-location-within-the-bundle.md).

##### Adopt Rpath Relative References

Not all code with a nonstandard structure is as accommodating as libWaffleVarnish.  For example, the build system for libRubPat expresses its dependencies using absolute paths:

```None
% otool -L "libRubPat/bin/rubpat"
…
    /usr/local/libRubPat/lib/libPat.dylib …
    /usr/local/libRubPat/lib/libRub.dylib …
    …
% otool -L "libRubPat/lib/libPat.dylib"
…
    /usr/local/libRubPat/lib/libPat.dylib …
    /usr/local/libRubPat/lib/libRub.dylib …
    …
% otool -L "libRubPat/lib/libRub.dylib"
…
    /usr/local/libRubPat/lib/libRub.dylib …
    …
```

This tool and its associated dynamic libraries will only work when they’re installed in `/usr/local/libRubPat`, so you can’t embed this code as-is in your bundle.

> **Note**: libWaffleVarnish, which is based entirely on rpath-relative paths, and libRubPat, which is based entirely on absolute paths, aren’t the only possibilities.  Many nonstandard code structures use a mishmash of absolute paths, relative paths, executable-relative paths (`@executable_path`), loader-relative paths (`@loader_path`), and rpath-relative paths (`@rpath`).  Sorting this out can be a challenge.

libWaffleVarnish, which is based entirely on rpath-relative paths, and libRubPat, which is based entirely on absolute paths, aren’t the only possibilities.  Many nonstandard code structures use a mishmash of absolute paths, relative paths, executable-relative paths (`@executable_path`), loader-relative paths (`@loader_path`), and rpath-relative paths (`@rpath`).  Sorting this out can be a challenge.

The best way to fix this problem is to update the code’s build system to use rpath-relative references.  However, this isn’t possible for libRubPat because that library is not open source.  To embed libRubPat in your bundle, use `install_name_tool` to change the paths embedded in its code items.  First remove all the code signatures:

```None
% codesign --remove-signature "libRubPat/lib/libRub.dylib"
% codesign --remove-signature "libRubPat/lib/libPat.dylib"
% codesign --remove-signature "libRubPat/bin/rubpat"
```

Changing code using `install_name_tool` breaks the seal on its code signature, a fact that `install_name_tool` warns you about.  You will be re-signing this code as part of your distribution process, so you might as well work with unsigned code and avoid a bunch of warnings.

Now change the dynamic library identifier for each library to be rpath-relative:

```None
% install_name_tool -id "@rpath/libRub.dylib" "libRubPat/lib/libRub.dylib"
% install_name_tool -id "@rpath/libPat.dylib" "libRubPat/lib/libPat.dylib"
```

This controls how the library identifies itself to the rest of the system.

Next, change each dynamic library dependency to match:

```None
% install_name_tool -change "/usr/local/libRubPat/lib/libRub.dylib" "@rpath/libWaffle.dylib" "libRubPat/lib/libPat.dylib"
% install_name_tool -change "/usr/local/libRubPat/lib/libRub.dylib" "@rpath/libWaffle.dylib" "libRubPat/bin/rubpat"
% install_name_tool -change "/usr/local/libRubPat/lib/libPat.dylib" "@rpath/libVarnish.dylib" "libRubPat/bin/rubpat"
```

Finally, add an executable-relative rpath to the tool:

```None
% install_name_tool -add_rpath "@executable_path/../lib" "libRubPat/bin/rubpat"
```

To confirm that you’ve fixed all the dependencies, run `otool` just like you did for libWaffleVarnish:

```None
% otool -l libRubPat/bin/rubpat | grep -B 1 -A 2 LC_RPATH 
Load command 17
          cmd LC_RPATH
      cmdsize 40
         path @executable_path/../lib (offset 12)

% otool -L "libRubPat/bin/rubpat"
…
    @rpath/libPat.dylib …
    @rpath/libRub.dylib …
    …
% otool -L "libRubPat/lib/libPat.dylib"
…
    @rpath/libPat.dylib …
    @rpath/libRub.dylib …
    …
% otool -L "libRubPat/lib/libRub.dylib"
…
    @rpath/libRub.dylib …
    …
```

The final result is a code structure where all the dynamic library dependencies are rpath-relative, and the rpath entry for the tool itself is executable-relative.  This structure works regardless of where it’s located on disk, making it feasible to embed it in your bundle.

##### Place Content in the Correct Location Within the Bundle

Once you’ve confirmed that the code uses rpath-relative paths, it’s time to embed it in your bundle.  Imagine you’re building an app called MacWaffleVarnish.  The rules in [`Placing content in a bundle`](https://developer.apple.com/documentation/BundleResources/placing-content-in-a-bundle) require this structure:

```None
MacWaffleVarnish.app/
  Contents/
    Info.plist
    MacOS/
      MacWaffleVarnish
      wafflevarnish
    Frameworks/
      libVarnish.dylib
      libWaffle.dylib
    Resources/
      … other resources …
      libWaffleVarnish/
        etc/
          wafflevarnish.config
```

The dynamic libraries are in `Contents/Frameworks`, the tool in `Contents/MacOS`, and the configuration file in `Contents/Resources`.

To make this work, use `install_name_tool` to adjust the rpath entry in the `wafflevarnish` tool to point to the Frameworks directory rather than the lib directory:

```None
% install_name_tool -rpath "@executable_path/../lib" "@executable_path/../Frameworks" "wafflevarnish"
```

And that’s all you need to do.  The use of rpath-relative references in libWaffleVarnish makes it easy to change its code structure to match platform conventions.

##### Use Symlinks for Gnarly Edge Cases

There’s one final gotcha here.  If you run the `wafflevarnish` tool you’ll see this error:

```None
% MacWaffleVarnish.app/Contents/MacOS/wafflevarnish
MacWaffleVarnish.app/Contents/MacOS/../etc/wafflevarnish.config: No such file or directory
…
```

It’s trying to access `wafflevarnish.config` via a path that’s relative to the executable, but you’ve moved things around such that the configuration file is no longer available at that relative path.  In many cases a tool will have a way to set the path to its configuration using a command-line argument or an environment variable.  If not, fix the problem using a symlink:

```None
MacWaffleVarnish.app/
  Contents/
    …
    MacOS/
      …
      wafflevarnish
    …
    Resources/
      …
      libWaffleVarnish/
        bin/
          wafflevarnish -> ../../MacOS/wafflevarnish
        etc/
          wafflevarnish.config
```

Now, if you run the `wafflevarnish` tool via the symlink, it finds the configuration file and all is well:

```None
% MacWaffleVarnish.app/Contents/Resources/libWaffleVarnish/bin/wafflevarnish
configuration:
  finish: gloss
…
```

Symlinking is a powerful technique for handling gnarly edge cases.  For example, if the code dynamically loads a plug-in via a relative path that leads to a location that cannot hold code, create a symlink at that location that points to where the code is actually placed.

You can also use symlinks to reduce the number of dynamic library dependencies you have to rewrite using `install_name_tool`.  Imagine you’re working with a huge code structure with a lot of inter-library dependencies.  Rather than rewrite all of those dependencies, you could embed the code structure en masse, then move each code item to its appropriate location within your bundle while leaving behind a symlink.

In most cases, however, it’s easier and better to rewrite everything to use rpath-relative references.

## See Also

- [Placing content in a bundle](../BundleResources/placing-content-in-a-bundle.md)
  Place bundle content in the correct location based on its type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/embedding-nonstandard-code-structures-in-a-bundle)*