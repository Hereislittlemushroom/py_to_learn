enum Visit{
    ReadOnly,
    write,
    executable
};

enum FileType{
    Folder,
    Document
};

#include<string>
class FCB {
public:
    string name;//文件名：    文件名.扩展名
    int nodeId;//文件标识：操作系统管理文件的唯一标识。
    FileType type;//文件类型：由扩展名给出。
    string path;//文件位置：文件所存放设备的具体位置。
    int size;//文件大小：以字节或块为单位的文件长度。
    Access access;//文件的保护方式：通常有读、写、执行等。
    string modifyDate;// 文件的创建或修改日期。
    FCB *index[N];//索引表
    FCB *father;//父节点
    FCB();
    ~FCB();
    string getTime();//获取系统时间

};

FCB::FCB() 
{
    this->access = Write;
    this->modifyDate = getTime();
    this->size = N;
}

FCB::~FCB()
{

}
string FCB::getTime()
{
    time_t t = time(0);
    char tmp[64];
    strftime(tmp, sizeof(tmp), "%Y/%m/%d %X", localtime(&t));
    return tmp;
}

