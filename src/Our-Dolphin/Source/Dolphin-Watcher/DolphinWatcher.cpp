#include "DolphinWatcher.h"
#include "../DolphinProcess/DolphinAccessor.h"
#include "../DolphinProcess/IDolphinProcess.h"
#include "../Common/CommonTypes.h"
#include "../Common/MemoryCommon.h"
#include <malloc.h>
#include <boost/lexical_cast.hpp>
#include <iostream>
#include "../MemoryWatch/MemWatchEntry.h"
#include <iostream>
#include <chrono>
typedef std::chrono::high_resolution_clock Clock;


namespace DolphinComm{


char* DolphinWatcher::get_raw_memory() {
    Common::MemOperationReturnCode code =m_Watch->readMemoryFromRAM();
    if (code != Common::MemOperationReturnCode::OK)
        std::cout << "Invalid read of: " << m_Watch->getConsoleAddress() << std::endl;
    return m_Watch -> getMemory();
    }    

std::string DolphinWatcher::status(){
        DolphinAccessor::DolphinStatus status =  m_Accesor->getStatus();
        return DolphinAccessor::statusString(status);
        }

DolphinAccessor::DolphinStatus DolphinWatcher::enum_status(){
    DolphinAccessor::DolphinStatus status =  m_Accesor->getStatus();
}


std::string DolphinWatcher::hook(){
    DolphinWatcher::m_Accesor-> hook();
    return this->status();
}    





std::string DolphinWatcher::getMemory(){
    return Common::formatMemoryToString(
        this->get_raw_memory(), m_Watch->getType(), 
        m_Watch->getLength()
        ,m_Watch->getBase(), false, false);}
        //Common::shouldBeBSwappedForType(m_Watch->getType()));}
     

int DolphinWatcher::watch(void){

    DolphinWatcher *d = new DolphinWatcher((u32) 0x80CAC434, 'w');
    while(true){
        d->hook();
        if ((d->enum_status())==DolphinAccessor::DolphinStatus::hooked){
           // auto t1= Clock::now();  
        std::string val = d->getMemory();
         //   auto t2= Clock::now();
       // std::cout << (t2-t1).count()/1000 << std::endl;
         std::cout << val << std::endl;
        //Common::formatMemoryToString(
        //     val, Common::MemType::type_byte, 1, Common::MemBase::base_decimal, false, false);
        // std::cout<<val_string<<std::endl;
        }
    }
    return 0;
}



} // namespace DolphinComm