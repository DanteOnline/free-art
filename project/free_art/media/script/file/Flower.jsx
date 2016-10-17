//author: dante
//http://danteonline.pythonanywhere.com

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

//функция вычисляет угол в зависимости от количества лепестков
function get_angle(count)
{
	return 2*Math.PI/count;
};

/*берем выделенный объект*/
selected_objects = app.activeDocument.selection;
//Если выделен 1 объект
if (selected_objects.length == 1)
{
	//получаем выделенный объект
	obj = selected_objects[0];
	//получаем документ
	document = app.activeDocument;
	//получаем размеры документа
	dh = document.height;
	dw = document.width;
	
	count = +prompt("Petals count:", 8);
	
	all_objects = get_copy_objects(obj, count);
	
	step_angle = +get_angle(count);
	angle = +0;
	
	radius = +prompt("radius:", (obj.width/(2*Math.tan(step_angle/2))));
	
	for (i=0;i<all_objects.length;++i)
	{
		l = +all_objects[i].height/2+radius;
		y=Math.sin(angle)*l;
		x=Math.cos(angle)*l;
		all_objects[i].top-=x;
		all_objects[i].left+=y;
		all_objects[i].rotate(180*angle/Math.PI);
		angle+=step_angle;
	}
	
	
}
else{
	alert("Выделите только один объект!");
}


