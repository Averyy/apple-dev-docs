# PostScript Injection Placement Options

**Framework**: Application Services  
**Kind**: tdef

Constants that specify where in the print job to inject PostScript code.

## Declaration

```c
typedef UInt16 PSInjectionPlacement;
enum {
   kPSInjectionBeforeSubsection = 1,
   kPSInjectionAfterSubsection = 2,
   kPSInjectionReplaceSubsection = 3
};
```

## Topics

### Constants
- [kPSInjectionBeforeSubsection](./postscript_injection_placement_options/kpsinjectionbeforesubsection.md)
  Specifies that your PostScript code be inserted before the standard PostScript code that is normally emitted for the subsection.
- [kPSInjectionAfterSubsection](./postscript_injection_placement_options/kpsinjectionaftersubsection.md)
  Specifies that your PostScript code be inserted after the standard PostScript code that is normally emitted for the subsection.
- [kPSInjectionReplaceSubsection](./postscript_injection_placement_options/kpsinjectionreplacesubsection.md)
  Specifies that your PostScript code replace the standard PostScript code that is normally emitted for the subsection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/postscript_injection_placement_options)*