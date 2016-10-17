function is_on_border(ol, or, ot, ob, h, w)
{
	var a = ((ob<0) && (ot>-h));
	var b = ((or>0) && (ol<w));
	if ((!a)||(!b))
	{
		return 2;
	}
	if (((ol < 0) && (or > 0)) || ((ol < w) && (or > w)) )
	{
		if (a)
		{
			//на границе
			return 1;
		}
		else
		{
			//за границей
			return 2;
		}
		
	}
	if (((ot > 0) && (ob < 0)) || ((ot > -h) && (ob < -h)))
	{
		if (b)
		{
			//на границе
			return 1;
		}
		else
		{
			//за границей
			return 2;
		}
	}
	return 0;
}

function process_objects(pageItems, newGroup, h, w)
{	
	var thisItem;
	for(var i = pageItems.length - 1; i > -1;  i--){  
            thisItem = pageItems[i]; 					
			res = is_on_border(thisItem.left, thisItem.left + thisItem.width, thisItem.top, thisItem.top - thisItem.height, h, w);
			if ((res==1)&&(thisItem!=newGroup))
			{		
				thisItem.move(newGroup, ElementPlacement.PLACEATBEGINNING); 			
			}
			else if (res==2)
			{
				thisItem.remove();
			}		   
        }; 
}

function ArtboardCrop(){  
    app.coordinateSystem = CoordinateSystem.ARTBOARDCOORDINATESYSTEM;  
    if(app.documents.length  > 0){  
        var doc = app.activeDocument;  
         
        var newGroup = doc.groupItems.add();  	
		h = doc.height;
		w = doc.width;

		process_objects(doc.layers[0].pageItems, newGroup, h, w);
		var activeArtboardIndex = doc.artboards.getActiveArtboardIndex();  
        var rc =  doc.artboards[activeArtboardIndex].artboardRect;  
        var newRect = doc.pathItems.rectangle(rc[1],rc[0],rc[2],-rc[3]);  
        newRect.filled = false;  
        newRect.stroked = false; 
		newRect.move(newGroup, ElementPlacement.PLACEATBEGINNING);
		newGroup.selected = true;
        //app.executeMenuCommand("selectall");  
		
        app.executeMenuCommand("Live Pathfinder Crop");  
        app.executeMenuCommand("expandStyle");  
    }  
}  
ArtboardCrop(); 
