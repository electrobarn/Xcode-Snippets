// singleton Pattern
// Pattern for dispatch_once-based singleton creation
// 
// Platform: All
// Language: Objective-C
// Completion Scope: Class Implementation

+ (<#class#> *)sharedObject {
    static <#class#> *_shared<#class#> = nil;
    static dispatch_once_t oncePredicate;
    dispatch_once(&oncePredicate, ^{
        
        _shared<#class#> = [[<#class#> alloc] init];
    });
    
    return _shared<#class#>;
}