#include <napi.h>
extern "C"
{
  #include "mylib.h"
}

std::string hello(){
  print();
  return "Hello World";
}

Napi::String HelloWrapped(const Napi::CallbackInfo& info)
{
  Napi::Env env = info.Env();
  Napi::String returnValue = Napi::String::New(env, hello());

  return returnValue;
}

Napi::Object InitAll(Napi::Env env, Napi::Object exports) {
  exports.Set("hello", Napi::Function::New(env, HelloWrapped));
  return exports;
}

NODE_API_MODULE(mylib, InitAll)
