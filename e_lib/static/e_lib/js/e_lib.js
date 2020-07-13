$(document).ready(function(){

    var urlsList = []; //list for storing elements id's
	// var newContent = ''; experimental list.

	$('ul').on('click', '.btn', function(e){

		// when an element of class .btn that is inside ul element is clicked ajax request gets triggered. 
		// console.log(newContent);

		e.stopPropagation();  //this prevents triggering of function when a child element of btn is clicked.
 
       const id = $(this).data('id')      //this gets data-id attribute value in in order to distinguish particular btn elements.
		if (!urlsList.includes(id)){      //when a btn is clicked first time its id is added to urlsList, then the folder is opened
			                              //ajax request fetches data from database and data is presented. When btn is clicked
			                              //the second time (i.e. urlsList includes the element's id) folder is closed, content 
			                              //removed and the id of the element is removed from the urlsList.
			urlsList.push(id);

			var list_html = '';          //for a string which will represent a folder list.
			var list_file_html = '';    //string that will represent a file list.
			Url = id,	
	        
			// console.log(url);
			$.ajax({
				'async': false,     //ajax request doesn't work without this line, but this apparently is not the best solution.
				url: Url,
				type: 'GET',
				// contentType: 'application/json',
				dataType: 'json',
				success: function(result) {     //here is what ajax will return
					
					list_html += "<ul>";       //beggining of the folder list
					list_file_html += "<ul>";

					for(var i=0; i < result.new_list.length; i++){ //is a JsonResponse returned by Django function. It is a json object of this form 
						                                           // {new_list: [ {}, {}, {}...]}

						if (result.new_list[i]['Link'] == undefined){   //checking whether the list element represents a file  or a folder. 

							//folder list content

						    list_html += "<li class=\"btn\" data-id='" + result.new_list[i]['Book_id'] +  "'><i class=\"fas fa-folder closed\" style= \"margin-right: 15px;\"></i><i class=\"fas fa-folder-open open\" style=\"margin-right: 15px;\"></i>"  + result.new_list[i]['Name'] + "</li><br>";
						    
					    } else {

					    	//file list content
	                        
	                        list_file_html += "<li class=\"btn\" data-id='" + result.new_list[i]['Book_id'] +  "'>"  + "<a href='" + result.new_list[i]['Link'] + "' target=\'_blank\'>" + result.new_list[i]['Name'] + "</a>" + "</li><br>";

	                        // console.log("This is a file"); 
					    }
					}

					list_html += "</ul>";  //
					list_file_html += "</ul>";
					
					}
	               
					
				// },

				// error: function(error){
				// 	console.log(`Error ${error}`)
				// }
	            	
			}) //closing ajax request block

	    $(this).append(list_html);                                //presenting the list of (sub)folders of current (this) folder.
        $(this).children('.closed').css('display', 'none');          // 'opening' the folder
        $(this).children('.open').css('display', 'inline-block');
        $('.col-md-6').children('ul').remove();        //remove currently displayed files (books) from the right hand side div.
        $('.col-md-6').prepend(list_file_html);  

        console.log('UrlsList: ',urlsList);
        console.log('UrlsList.length: ',urlsList.length);

        var index_list = [];

	    for(let i = 0; i < urlsList.length; i++){
	    		
            if (urlsList[i] != id && $(this).parents(`li[data-id="${urlsList[i]}"]`).length != 1){
            	console.log('Item not clicked')
            	$(`li[data-id="${urlsList[i]}"]`).children('ul').remove();
            	$(`li[data-id="${urlsList[i]}"]`).children('.open').css('display', 'none');
            	console.log('urlsList[i]: ', urlsList[i])
            	console.log($(this).data('id'))
            	$(`li[data-id="${urlsList[i]}"]`).children('.closed').css('display', 'inline-block');
            	index_list.push(i) //ova linija uzrokuje da petlja stane nakon prvog kruga. Da bi normalno funkcionisala ovo mora da ide izvan petlje.
            	console.log('UrlsList.length: ',urlsList.length)

            } else{
            	console.log('Item clicked')
            }
            
	    }

	    for(let i = index_list.length - 1; i >= 0; i--){
            urlsList.splice(index_list[i], 1);  
        }
	    
	   


	} else {                                     //this block is executed on the second click of the same btn element (folder).
			$(this).children('ul').remove();         //subfolders are removed/
			i = urlsList.indexOf(id);                //id of the element is removed from the urlsList.
			urlsList.splice(i, 1);
			// newContent = '';
			$('.col-md-6').children('ul').remove();               //books currently displayed on the right hand side are removed.

	        $(this).children('.open').css('display', 'none');            //folder (icon) closed.
	        $(this).children('.closed').css('display', 'inline-block');
	        
		}

    })

})

