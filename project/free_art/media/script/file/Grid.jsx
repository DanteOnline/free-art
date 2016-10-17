//author: dante
//http://danteonline.pythonanywhere.com


//находим максимальный размер
//obj - объект с которым мы работаем
function get_max_size(obj)
{
	objw = obj.width;
	objh = obj.height;
	if (objw>objh)
	{
		return objw;
	}
	else
	{
		return objh;
	}
};

//копируем объект и возвращаем набор объектов
//obj - объект, который мы копируем
//count - итоговое количество
function get_copy_objects(obj, count)
{
	//создаем массив оъектов
	var objs = new Array();
	//добавляем в него сам объект
	objs.push(obj);
	//копируем объект count-1 раза
	for (i=0;i<count-1;++i)
	{
		D = obj.duplicate();
		objs.push(D);
	}
	return objs;
};

//рассчет количества объектов
//objs размер объекта
//ds размер домкумента
function calc_objects_cnt(objs, ds)
{
	var cnt = ds/objs;
	var cntf = Math.floor(cnt);
	return cntf;
};

//расчет шага
//cnt - количество объектов
function calc_step(cnt, ds)
{
	return ds/cnt;
}

/*берем выделенный объект*/
selected_objects = app.activeDocument.selection;
//Если выделен 1 объект
if (selected_objects.length == 1)
{
	//получаем выделенный объект
	obj = selected_objects[0];
	//получаем размеры объекта
	objw = +obj.width;
	objh = +obj.height;
	//получаем документ
	document = app.activeDocument;
	//получаем размеры документа
	dh = document.height;
	dw = document.width;
	//просим ввести шаг
	//step = prompt("Введите шаг расстановки",1);
	
	//считаем максимальное количетво объектов
	cwm = +calc_objects_cnt(objw, dw);
	chm = +calc_objects_cnt(objh, dh);
	cwm+=+1;
	chm+=+1;
	
	//просим ввести сколько будет объектов (не больше максимального кол-ва)
	cw = +prompt("Objetcs count horizontally:",cwm);
	ch = +prompt("Objetcs count vertically:",chm);
	
	//считаем шаги
	stepw = +calc_step(cw-1,dw);
	steph = +calc_step(ch-1,dh);
	
	//создаем объекты
	all_cnt = cw*ch;
	all_objects = get_copy_objects(obj, all_cnt);
	
	//рисуем объекты
	startx = -objw/2;
	starty = +objh/2;
	
	var k = +0;
	for (i=0;i<cw;++i)
	{
		for (j=0;j<ch;++j)
		{
			all_objects[k].top = starty;	
			all_objects[k].left = startx;
			starty-=steph;
			//starty-=objh;
			k+=+1;
		}
		startx+=+stepw;
		//startx+=+objw;
		starty=+objh/2;
		
	}
}
else{
	alert("Выделите только один объект!");
}


