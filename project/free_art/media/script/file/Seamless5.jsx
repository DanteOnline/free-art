//author: dante
//http://danteonline.pythonanywhere.com

/*берем выделенный объект*/
selected_objects = app.activeDocument.selection;
//Если выделен 1 объект
if (selected_objects.length == 1)
{
	//получаем выделенный объект
	obj = selected_objects[0];
	//получаем размеры объекта
	objw = obj.width;
	objh = obj.height;
	//получаем документ
	document = app.activeDocument;
	//получаем размеры документа
	dh = document.height;
	dw = document.width;
	
	var objs = new Array();
	objs.push(obj);
	//копируем объект 4 раза
	for (i=0;i<4;++i)
	{
		D = obj.duplicate();
		objs.push(D);
	}	
	
	//получаем все выделенные объекты
	all_objects = objs;
	
	if (all_objects.length == 5)
	{
	//левый верхний
		obj_lt = all_objects[0];
		obj_lt.top = objh/2;
		obj_lt.left = -objw/2;
	//правый верхний
		obj_lt = all_objects[1];
		obj_lt.top = objh/2;
		obj_lt.left = dw-objw/2;
	//левый нижний
		obj_lt = all_objects[2];
		obj_lt.top = -dh+objh/2;
		obj_lt.left = -objw/2;
	//правый нижний
		obj_lt = all_objects[3];
		obj_lt.top = -dh+objh/2;
		obj_lt.left = dw-objw/2;
	//центральный
		obj_lt = all_objects[4];
		obj_lt.top = -dh/2+objh/2;
		obj_lt.left = dw/2-objw/2;
	}
	else{
		alert("На рисунке лишние объекты, нужно оставить только 1")
	}
	
	
}
else{
	alert("Выделите только один объект!");
}


