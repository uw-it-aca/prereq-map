<template>
<div class="card" id="infobox">
    <div class="card-header bg-white">
        <h5 class="infobox-title">{{ course }}</h5>
        <span class="card-close clickable close-icon" data-effect="fadeOut"><i class="fas fa-times"></i></span>
        <p class="card-title">Lorem ipsum dolor set amet dapibus ac facilisis in</p>
    </div>
    <div class="card-header card-body">
        <h6 class="card-title">Has these prerequisites<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#"
                    data-original-title="Declared Majors"></i></span></h6>
        <ol class="list-group list-group-flush">
            <li class="#">ACCTG 225</li>
            <li class="#">ECON 200</li>
            <li class="#">
                One of MATH 112, MATH 124, MATH 125, MATH 134, MATH 135, or Q SCI 291</li>
            <li class="#">One of ECON 311, IND E 315, QMETH 201, Q SCI 291, Q SCI 381, PSYCH 315, PSYCH 318, STAT 220, STAT 221/SOC 221/CS&SS 221, STAT 311, or STAT 390; </li>
        </ol>
    </div>
    <div class="card-header card-body">
        <h5 class="card-title">Is a prerequisite for<span class="info-popover"><i class="fa fa-info-circle" aria-hidden="true" tabindex="0" data-placement="top" data-toggle="popover" data-trigger="focus" title="" data-content="#" data-original-title="Declared Majors"></i></span></h5>
        <ul class="list-inline comma-list">
            <li class="#">ABCD 123</li>
            <li class="#">ZYX 123</li>
            <li class="#">ABCD 123</li>
            <li class="#">ZYX 123</li>
            <li class="#">ABCD 123</li>
        </ul>
    </div>
    <div class="card-body text-center">
        <a href="/course-search/?course=cse%20373" class="btn btn-primary btn-block btn-lg btn-default">More details &amp; related curricula</a>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            course: 'Course XXX1235'
        }
    }
}
</script>

<style lang="scss" scoped>
.card {
    color: red;
}
</style>
