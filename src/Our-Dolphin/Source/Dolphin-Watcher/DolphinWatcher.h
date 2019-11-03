#include "../DolphinProcess/DolphinAccessor.h"
#include "../DolphinProcess/IDolphinProcess.h"
#include "../Common/CommonTypes.h"
#include "../Common/MemoryCommon.h"
#include "../malloc.h"
#include "../MemoryWatch/MemWatchEntry.h"



namespace DolphinComm
{
    class DolphinWatcher{

        private:
            DolphinAccessor* m_Accesor;
            MemWatchEntry* m_Watch;
            u64 emuRamStartAdress;
            char * m_buff; 
            char* get_raw_memory(); 
            //static Common::MemType strToType(char c);
            
            
            
        public:
            
            static int watch();
            std::string getMemory();
            std::string hook();
            std::string status();
            DolphinAccessor::DolphinStatus enum_status();

        static Common::MemType strToType(char c){
            switch (c)
            {
            case 'b':
                return Common::MemType::type_byte;
                break;
            
            case 'h':
                return Common::MemType::type_halfword;

            case 'f':
                return Common::MemType::type_float;

            case 'd':
                return Common::MemType::type_double;
            
            case 'w':
                return Common::MemType::type_word;

            default:
                std::__throw_invalid_argument("Invalid type specifier");
            }
        }    
        
        
        DolphinWatcher(u32 adress, char ttype){
            m_Accesor=new DolphinAccessor;
            m_Watch = new MemWatchEntry();
            m_Watch ->setConsoleAddress(adress);
            m_Watch ->setTypeAndLength(DolphinWatcher::strToType(ttype),1);
            m_Accesor -> hook();
            DolphinWatcher::emuRamStartAdress = m_Accesor->getEmuRAMAddressStart();
        }

    };
} // namespace DolphinCommon

