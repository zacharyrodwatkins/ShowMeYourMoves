#include <boost/python.hpp>
#include "Dolphin-Watcher/DolphinWatcher.h"
using namespace boost::python;


BOOST_PYTHON_MODULE(DolphinMemoryEngine)
{
    Py_Initialize();
    class_<DolphinComm::DolphinWatcher>("MemoryWatcher",init<uint32_t, char>())
    .def("hook", &DolphinComm::DolphinWatcher::hook)
    .def("getStatus", &DolphinComm::DolphinWatcher::status)
    .def("getMemory", &DolphinComm::DolphinWatcher::getMemory);

}
