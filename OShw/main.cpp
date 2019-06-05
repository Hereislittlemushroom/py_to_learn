#include<iostream>
#include<stdlib.h>
using namespace std;
 
#define MAXSIZE 1000
enum status { FREE, BUSY };
 
typedef struct freespace
{
	int num;         //分区号
	int size;        //分区大小
	int address;     //分区首地址
	status state;    //分区状态，FREE和BUSY
}freespace;
 
typedef struct node
{
	freespace data;
	node *head;
	node *next;
}*Linklist;
 
Linklist first,last;
Linklist p0,p1,p2,p3,p4,p5;
 
void initial()
{
	first = new node;
	last = new node;
	first->head = NULL;
	first->next = last;
	last->head = first;
	last->next = NULL;
	last->data.address = 0;
	last->data.size = MAXSIZE;
	last->data.num = 0;
	last->data.state = FREE;
	
	/*
	p0->head=first;
	p0->next=first->next;
	first->next->head=p0;
	first->next=p0;
	
	
	last->next=p0;
	p0->head=last;
	p0->next=NULL;

	p0->data.num=0;
	p0->data.address=1;
	p0->data.size=32;
	p0->data.state=FREE;
	*/
}
 
void display()
{
	cout << "--------------------主内存分配情况--------------------" << endl;
	node *p = first->next;
	while (p)
	{
		cout << "分区号：";
		if (p->data.num == 0)
		{
			cout << "空闲区" << "  " << "起始地址：" << p->data.address << "	" << "终止地址：" << p->data.address+p->data.size<<
				"	" << "分区大小：" <<
				p->data.size << "KB" << "	" << "状态:空闲" << endl;
		}
		else
		{
			cout << p->data.num;
			cout << "	" << "起始地址：" << p->data.address << "	" << "终止地址：" << p->data.address + p->data.size << "	"
				"分区大小：" << p->data.size
				<< "KB" << "	" << "状态:";
			if (p->data.state == FREE)
				cout << "空闲" << endl;
			else if (p->data.state == BUSY)
				cout << "占用" << endl;
		}
		p = p->next;
	}
	cout << "-----------------------------------------------------" << endl << endl;
}
 
int firstAlloc(int num,int size,int address)//首次分配
{
//	int num, size;
//	cout << "请输入作业号和分配的主存大小KB：" << endl;;
//	cin >> num >> size;
	Linklist list = new node;
	list->data.num = num;
	list->data.size = size;
	list->data.state = BUSY;
	list->data.address= address;
	node *p = first->next;
	while (p)
	{
		if (p->data.state == FREE&&p->data.size == size)//有大小刚好合适的空闲块
		{
			p->data.state = BUSY;
			p->data.num = num;
			display();
			return 1;
		}
		if (p->data.state == FREE&&p->data.size > size)//有大小比他大的空闲块
		{
			list->head = p->head;
			list->next = p;
			list->data.address = p->data.address;
			p->head->next = list;
			p->head = list;
			p->data.address = list->data.address + list->data.size;
			p->data.size -= size;
			display();
			return 1;
		}
		p = p->next;
	}
	display();
	return 0;
}
 

int recycle(int num)//碎片整理
{
//	int num;
//	cout << "请输入你要回收内存的作业号：" << endl;
//	cin >> num;
	node *p = first;
	while (p)
	{
		if (p->data.num == num)
		{
			p->data.state = FREE;
			p->data.num = 0;
			if (p->head->data.state == FREE)//与前一块空闲区相邻，则合并
			{
				p->head->data.size += p->data.size;
				p->head->next = p->next;
				p->next->head = p->head;
			}
			if (p->next->data.state == FREE)//与后一块空闲区相邻，则合并
			{
				p->data.size += p->next->data.size;
				p->next->next->head = p;
				p->next = p->next->next;
			}
			break;
		}
		p = p->next;
	}
	display();
	return 1;
}
 
void menu()
{
	cout << "--------------------内存分配系统--------------------" << endl;
	cout << "*              1.分配内存                          *" << endl;
	cout << "*              2.查看主存分配情况                  *" << endl;
	cout << "*              3.回收主存                          *" << endl;
	cout << "----------------------------------------------------" << endl;
	cout << "请选择：" << endl;
}
 
int main()
{
	initial();
	int choose;
	while (1)
	{
		menu();
		cin >> choose;
		switch (choose)
		{
		case 1:
			firstAlloc(1,32,3);
			firstAlloc(2,10,40);
			firstAlloc(3,15,60);
			firstAlloc(4,228,100);
			firstAlloc(5,100,500);
			firstAlloc(0,1,700);
			break;
		case 2:
			display();
			break;
		case 3:
			cout<<"请依次输入要回收的作业编号"<<endl; 
			int array[10];
			for(int i=1; i<=5;i++)
				cin>>array[i];	
			for(int i=1; i<=5;i++)
				recycle(array[i]);	
			break;
		default :
			cout << "请输入有效数字！" << endl;
			break;
		}
	}
}

