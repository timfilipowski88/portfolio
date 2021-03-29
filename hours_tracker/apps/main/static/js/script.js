$(document).ready(function(){
        // fill out collections in collections tab table when nav button is clicked
    $('#pills-collections-tab').on("click", function(res){
        console.log('hello world')
        $.ajax({
            url: '/main/get_collection_form',
            method: 'GET',
            success: function(res) {
                console.log(res)
                $('#collections_table_body').html(res)
            }
        })
    });
        // fill out assignments in assignments tab table when nav button is clicked
    $('#pills-assignments-tab').on("click", function(res){
        console.log('hello world')
        $.ajax({
            url: '/main/get_assignment_form',
            method: 'GET',
            success: function(res) {
                console.log(res)
                $('#assignments_table_body').html(res)
            }
        })
    });

    // add assignment, needs success or failure json responses 
    $('#add_assignment').submit(function(e){
        console.log(e)
        e.preventDefault()
        $.ajax({
            url: '/main/add_assignment/',
            method: 'POST',
            data: $(this).serialize(),
            success: function(res){
                console.log(res)
                $('#assignments_table_body').append(res)
            },
            error: function(err){
                console.error(err)
            }
        })
        $(this).trigger('reset')
    });

// add collection
    $('#add_collection').submit(function(e){
        e.preventDefault()
        $.ajax({
            url: '/main/add_collection/',
            method: 'POST',
            data: $(this).serialize(),
            success: function(res){
                $('#collections_table_body').append(res)
            }
        })
    });

//  update assignment
    $('.update_assignment').submit(function(e){
        e.preventDefault()
        $.ajax({
            url: "{% url 'update_assigment' %}",
            method: 'POST',
            data: $(this).serialize(res),
            success: function(res){
                $('#assignments_table_body').html(res)
            }
        })
    });

});


// Get future_date
// find all complete=False assignments_due with due_date less than future date
// get days_available, if null equal to total number of days between date_now and future_date
// Get total_min and total_max
// Average those assignments_due min and max values according to days_available
// context = { total_min, total_max, average_min, average_max, days_available, future_date}
