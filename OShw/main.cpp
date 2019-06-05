#include<iostream>
#include<stdlib.h>
using namespace std;
 
#define MAXSIZE 1000
enum status { FREE, BUSY };
 
typedef struct freespace
{
	int num;         //������
	int size;        //������С
	int address;     //�����׵�ַ
	status state;    //����״̬��FREE��BUSY
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
	cout << "--------------------���ڴ�������--------------------" << endl;
	node *p = first->next;
	while (p)
	{
		cout << "�����ţ�";
		if (p->data.num == 0)
		{
			cout << "������" << "  " << "��ʼ��ַ��" << p->data.address << "	" << "��ֹ��ַ��" << p->data.address+p->data.size<<
				"	" << "������С��" <<
				p->data.size << "KB" << "	" << "״̬:����" << endl;
		}
		else
		{
			cout << p->data.num;
			cout << "	" << "��ʼ��ַ��" << p->data.address << "	" << "��ֹ��ַ��" << p->data.address + p->data.size << "	"
				"������С��" << p->data.size
				<< "KB" << "	" << "״̬:";
			if (p->data.state == FREE)
				cout << "����" << endl;
			else if (p->data.state == BUSY)
				cout << "ռ��" << endl;
		}
		p = p->next;
	}
	cout << "-----------------------------------------------------" << endl << endl;
}
 
int firstAlloc(int num,int size,int address)//�״η���
{
//	int num, size;
//	cout << "��������ҵ�źͷ���������СKB��" << endl;;
//	cin >> num >> size;
	Linklist list = new node;
	list->data.num = num;
	list->data.size = size;
	list->data.state = BUSY;
	list->data.address= address;
	node *p = first->next;
	while (p)
	{
		if (p->data.state == FREE&&p->data.size == size)//�д�С�պú��ʵĿ��п�
		{
			p->data.state = BUSY;
			p->data.num = num;
			display();
			return 1;
		}
		if (p->data.state == FREE&&p->data.size > size)//�д�С������Ŀ��п�
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
 

int recycle(int num)//��Ƭ����
{
//	int num;
//	cout << "��������Ҫ�����ڴ����ҵ�ţ�" << endl;
//	cin >> num;
	node *p = first;
	while (p)
	{
		if (p->data.num == num)
		{
			p->data.state = FREE;
			p->data.num = 0;
			if (p->head->data.state == FREE)//��ǰһ����������ڣ���ϲ�
			{
				p->head->data.size += p->data.size;
				p->head->next = p->next;
				p->next->head = p->head;
			}
			if (p->next->data.state == FREE)//���һ����������ڣ���ϲ�
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
	cout << "--------------------�ڴ����ϵͳ--------------------" << endl;
	cout << "*              1.�����ڴ�                          *" << endl;
	cout << "*              2.�鿴����������                  *" << endl;
	cout << "*              3.��������                          *" << endl;
	cout << "----------------------------------------------------" << endl;
	cout << "��ѡ��" << endl;
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
			cout<<"����������Ҫ���յ���ҵ���"<<endl; 
			int array[10];
			for(int i=1; i<=5;i++)
				cin>>array[i];	
			for(int i=1; i<=5;i++)
				recycle(array[i]);	
			break;
		default :
			cout << "��������Ч���֣�" << endl;
			break;
		}
	}
}

