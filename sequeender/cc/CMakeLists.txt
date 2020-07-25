# glob headers for cppyy to parse
file(GLOB_RECURSE HEADER_FILES
     #     RELATIVE ${CMAKE_SOURCE_DIR}
     CONFIGURE_DEPENDS
     ${CMAKE_CURRENT_LIST_DIR}/*.h)
foreach (path ${HEADER_FILES})
  list(APPEND LIB_HEADERS ${path})
endforeach ()
set(LIB_HEADERS ${LIB_HEADERS} PARENT_SCOPE)

# please sort the source files alphabetically
add_library(${CMAKE_PROJECT_NAME}
            SHARED
            arcsort.cc
            aux_labels.cc
            connect.cc
            determinize.cc
            fsa.cc
            fsa_equivalent.cc
            fsa_renderer.cc
            fsa_util.cc
            intersect.cc
            properties.cc
            rmepsilon.cc
            topsort.cc
            util.cc
            weights.cc
            )

set_target_properties(${CMAKE_PROJECT_NAME}
                      PROPERTIES
                      LINKER_LANGUAGE
                      CXX)

set_target_properties(${CMAKE_PROJECT_NAME}
                      PROPERTIES
                      VERSION ${PROJECT_VERSION}
                      SOVERSION 1
                      )

set_target_properties(${CMAKE_PROJECT_NAME}
                      PROPERTIES
                      PUBLIC_HEADER
                      ${LIB_HEADERS})

target_include_directories(${CMAKE_PROJECT_NAME}
                           PUBLIC
                           ${CMAKE_SOURCE_DIR}
                           ${CMAKE_CURRENT_LIST_DIR})

#if (CMAKE_VERSION VERSION_LESS 3.8)
#  set(CMAKE_CXX_STANDARD 11)
#  set(CMAKE_CXX_STANDARD_REQUIRED ON)
#  set(CMAKE_CXX_EXTENSIONS OFF)
#else ()
#  target_compile_features(${CMAKE_PROJECT_NAME} PUBLIC cxx_std_11)
#endif ()

target_link_libraries(${CMAKE_PROJECT_NAME} PUBLIC glog)

function(sequeender_add_fsa_test name)
  add_executable(${name} "${name}.cc")
  target_link_libraries(${name}
                        PRIVATE
                        ${CMAKE_PROJECT_NAME}
                        gtest
                        gtest_main
                        )
  add_test(NAME "Test.${name}"
           COMMAND
           $<TARGET_FILE:${name}>
           )
endfunction()

# please sort the source files alphabetically
set(fsa_tests
    arcsort_test
    array_test
    aux_labels_test
    connect_test
    determinize_test
    fsa_equivalent_test
    fsa_renderer_test
    fsa_test
    fsa_util_test
    intersect_test
    properties_test
    rmepsilon_test
    topsort_test
    weights_test
    )

foreach (name IN LISTS fsa_tests)
  sequeender_add_fsa_test(${name})
endforeach ()
