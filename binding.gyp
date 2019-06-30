{
    "targets": [
        {
            "target_name": "mylib",
            "cflags!": [
                "-fno-exceptions"
            ],
            "cflags_cc!": [
                "-fno-exceptions"
            ],
            "sources": [
                "native-src/napi-wrapper.cpp"
            ],
            'include_dirs': [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            'libraries': [
                "-lmylib",
                "-L$(lib_dir)"
            ],
            'dependencies': [
                "<!(node -p \"require('node-addon-api').gyp\")"
            ],
            'defines': [
                'NAPI_DISABLE_CPP_EXCEPTIONS'
            ]
        }
    ]
}
