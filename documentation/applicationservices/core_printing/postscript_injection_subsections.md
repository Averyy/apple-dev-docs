# PostScript Injection Subsections

**Framework**: Application Services  
**Kind**: tdef

Constants that specify PostScript injection values for the subsection key.

## Declaration

```c
typedef SInt32 PSInjectionSubsection;
enum {
   kInjectionSubPSAdobe = 1,
   kInjectionSubPSAdobeEPS = 2,
   kInjectionSubBoundingBox = 3,
   kInjectionSubEndComments = 4,
   kInjectionSubOrientation = 5,
   kInjectionSubPages = 6,
   kInjectionSubPageOrder = 7,
   kInjectionSubBeginProlog = 8,
   kInjectionSubEndProlog = 9,
   kInjectionSubBeginSetup = 10,
   kInjectionSubEndSetup = 11,
   kInjectionSubBeginDefaults = 12,
   kInjectionSubEndDefaults = 13,
   kInjectionSubDocFonts = 14,
   kInjectionSubDocNeededFonts = 15,
   kInjectionSubDocSuppliedFonts = 16,
   kInjectionSubDocNeededRes = 17,
   kInjectionSubDocSuppliedRes = 18,
   kInjectionSubDocCustomColors = 19,
   kInjectionSubDocProcessColors = 20,
   kInjectionSubPlateColor = 21,
   kInjectionSubPageTrailer = 22,
   kInjectionSubTrailer = 23,
   kInjectionSubEOF = 24,
   kInjectionSubBeginFont = 25,
   kInjectionSubEndFont = 26,
   kInjectionSubBeginResource = 27,
   kInjectionSubEndResource = 28,
   kInjectionSubPage = 29,
   kInjectionSubBeginPageSetup = 30,
   kInjectionSubEndPageSetup = 31
};
```

## Topics

### Constants
- [kInjectionSubPSAdobe](./postscript_injection_subsections/kinjectionsubpsadobe.md)
  Specifies the “%!PS-Adobe” subsection.
- [kInjectionSubPSAdobeEPS](./postscript_injection_subsections/kinjectionsubpsadobeeps.md)
  Specifies the “%!PS-Adobe-3.0 EPSF-3.0” subsection.
- [kInjectionSubBoundingBox](./postscript_injection_subsections/kinjectionsubboundingbox.md)
  Specifies the “%BoundingBox” subsection.
- [kInjectionSubEndComments](./postscript_injection_subsections/kinjectionsubendcomments.md)
  Specifies the “%EndComments” subsection.
- [kInjectionSubOrientation](./postscript_injection_subsections/kinjectionsuborientation.md)
  Specifies the “%Orientation” subsection.
- [kInjectionSubPages](./postscript_injection_subsections/kinjectionsubpages.md)
  Specifies the “%Pages” subsection.
- [kInjectionSubPageOrder](./postscript_injection_subsections/kinjectionsubpageorder.md)
  Specifies the “%PageOrder” subsection.
- [kInjectionSubBeginProlog](./postscript_injection_subsections/kinjectionsubbeginprolog.md)
  Specifies the “%BeginProlog” subsection.
- [kInjectionSubEndProlog](./postscript_injection_subsections/kinjectionsubendprolog.md)
  Specifies the “%EndProlog” subsection.
- [kInjectionSubBeginSetup](./postscript_injection_subsections/kinjectionsubbeginsetup.md)
  Specifies the “%BeginSetup” subsection.
- [kInjectionSubEndSetup](./postscript_injection_subsections/kinjectionsubendsetup.md)
  Specifies the “%EndSetup” subsection.
- [kInjectionSubBeginDefaults](./postscript_injection_subsections/kinjectionsubbegindefaults.md)
  Specifies the “%BeginDefaults” subsection.
- [kInjectionSubEndDefaults](./postscript_injection_subsections/kinjectionsubenddefaults.md)
  Specifies the “%EndDefaults” subsection.
- [kInjectionSubDocFonts](./postscript_injection_subsections/kinjectionsubdocfonts.md)
  Specifies the “%DocumentFonts” subsection.
- [kInjectionSubDocNeededFonts](./postscript_injection_subsections/kinjectionsubdocneededfonts.md)
  Specifies the “%DocumentNeededFonts” subsection.
- [kInjectionSubDocSuppliedFonts](./postscript_injection_subsections/kinjectionsubdocsuppliedfonts.md)
  Specifies the “%DocumentSuppliedFonts” subsection.
- [kInjectionSubDocNeededRes](./postscript_injection_subsections/kinjectionsubdocneededres.md)
  Specifies the “%DocumentNeededResources” subsection.
- [kInjectionSubDocSuppliedRes](./postscript_injection_subsections/kinjectionsubdocsuppliedres.md)
  Specifies the “%DocumentSuppliedResources” subsection.
- [kInjectionSubDocCustomColors](./postscript_injection_subsections/kinjectionsubdoccustomcolors.md)
  Specifies the “%DocumentCustomColors” subsection.
- [kInjectionSubDocProcessColors](./postscript_injection_subsections/kinjectionsubdocprocesscolors.md)
  Specifies the “%DocumentProcessColors” subsection.
- [kInjectionSubPlateColor](./postscript_injection_subsections/kinjectionsubplatecolor.md)
  Specifies the “%PlateColor” subsection.
- [kInjectionSubPageTrailer](./postscript_injection_subsections/kinjectionsubpagetrailer.md)
  Specifies the “%PageTrailer” subsection.
- [kInjectionSubTrailer](./postscript_injection_subsections/kinjectionsubtrailer.md)
  Specifies the “%Trailer” subsection.
- [kInjectionSubEOF](./postscript_injection_subsections/kinjectionsubeof.md)
  Specifies the “%EOF” (end of file) subsection.
- [kInjectionSubBeginFont](./postscript_injection_subsections/kinjectionsubbeginfont.md)
  Specifies the “%BeginFont” subsection.
- [kInjectionSubEndFont](./postscript_injection_subsections/kinjectionsubendfont.md)
  Specifies the “%EndFont” subsection.
- [kInjectionSubBeginResource](./postscript_injection_subsections/kinjectionsubbeginresource.md)
  Specifies the “%BeginResource” subsection.
- [kInjectionSubEndResource](./postscript_injection_subsections/kinjectionsubendresource.md)
  Specifies the “%EndResource” subsection.
- [kInjectionSubPage](./postscript_injection_subsections/kinjectionsubpage.md)
  Specifies the “%Page” subsection.
- [kInjectionSubBeginPageSetup](./postscript_injection_subsections/kinjectionsubbeginpagesetup.md)
  Specifies the “%BeginPageSetup” subsection.
- [kInjectionSubEndPageSetup](./postscript_injection_subsections/kinjectionsubendpagesetup.md)
  Specifies the “%EndPageSetup” subsection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/core_printing/postscript_injection_subsections)*