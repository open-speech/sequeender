#
# Set up the Cppyy bindings generation. This is a customized version defined
# in boink's cmake/ dir; it uses genreflex rather than calling rootcling directly.
# I did this because I couldn't get rootcling to properly include/exclude classes
# via the LinkDef header, and I wanted to be able to use the better syntax in
# the genreflex selection XML anyhow. Also, I think this is now the recommended /
# more modern way anyhow? Code was modified from the versions cppyy distributes.
#

get_target_property(glog_INCLUDE_PATH glog INCLUDE_DIRECTORIES)
foreach (path ${glog_INCLUDE_PATH})
  list(APPEND glog_INCLUDE_DIRS ${path})
endforeach ()

cppyy_add_bindings(
    "${CMAKE_PROJECT_NAME}" "${PROJECT_VERSION}" "Meixu Song" "songmeixu@outlook.com"
    LICENSE "MIT"
    LANGUAGE_STANDARD "14"
    SELECTION_XML ${CMAKE_CURRENT_LIST_DIR}/selection.xml
    INTERFACE_FILE ${CMAKE_SOURCE_DIR}/${CMAKE_PROJECT_NAME}/cc/fsa.h
    HEADERS ${LIB_HEADERS}
    INCLUDE_DIRS ${CMAKE_SOURCE_DIR}
                 ${CMAKE_SOURCE_DIR}/${CMAKE_PROJECT_NAME}/cc
                 ${glog_INCLUDE_DIRS}
    LINK_LIBRARIES ${CMAKE_PROJECT_NAME}
    NAMESPACES ${CMAKE_PROJECT_NAME}
)

install(TARGETS "${CMAKE_PROJECT_NAME}"
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}/${CMAKE_PROJECT_NAME}
        )

install(CODE "execute_process(COMMAND pip install ${PY_WHEEL_FILE})")
