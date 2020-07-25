# please sort the files alphabetically
pybind11_add_module(_sequeender
  array.cc
  fsa.cc
  fsa_util.cc
  sequeender.cc
  tensor.cc
)

target_include_directories(_sequeender PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(_sequeender PRIVATE ${CMAKE_PROJECT_NAME})
